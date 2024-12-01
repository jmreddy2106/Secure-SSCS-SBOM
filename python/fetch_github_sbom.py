import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import time
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor
import requests
from pathlib import Path
import json 
from tabulate import tabulate


"""
created by : @author: https://github.com/jmreddy2106

Description:

This Python script automates the process of fetching Software Bill of Materials (SBOM) data for repositories from GitHub, storing the data in a PostgreSQL database, and handling rate limits effectively. It is designed to work in environments where automation of dependency tracking and SBOM management is required. The script supports asynchronous operations to improve efficiency when interacting with GitHub APIs. The primary key is not the repository name in the database. Since, there is a continuous development of a project and script need to fetch the SBOM data may be every day or every week. Based on the requirement, you can run this script as cron job or any other scheduler. Furthermore, to analyse any SBOM, get the latest timestamp of a repo from the database.

"""

# Determine the project's root directory
ROOT_DIR = Path(__file__).resolve().parent.parent

# Load the .env file from the root directory
load_dotenv(ROOT_DIR / '.env')

GITHUB_OWNER = os.getenv('GITHUB_OWNER')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
DB_CONNECTION = os.getenv('DB_CONNECTION')  # PostgreSQL connection string

BASE_URL = 'https://api.github.com/repos/'

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}

REQUIRED_FILES = {"package.json", "requirements.txt"}


def verify_or_create_database_and_table():
    """Verify if the database and table exist, create them if not."""
    try:
        with psycopg2.connect(DB_CONNECTION) as conn:
            conn.autocommit = True  # Allow creation of the database
            with conn.cursor() as cursor:
                # Check if the `sbom_data` table exists
                cursor.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE table_name = 'sbom_data'
                    );
                """)
                table_exists = cursor.fetchone()[0]

                # Create the `sbom_data` table if it doesn't exist
                if not table_exists:
                    print("Table 'sbom_data' does not exist. Creating it now...")
                    cursor.execute("""
                        CREATE TABLE sbom_data (
                            id SERIAL PRIMARY KEY,
                            repo_owner varchar(500) NOT NULL,
                            reponame varchar(500) NOT NULL,
                            sbom JSONB NOT NULL,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        );
                    """)
                    print("Table 'sbom_data' created successfully.")
                else:
                    print("Table 'sbom_data' already exists.")
    except psycopg2.Error as db_error:
        print(f"Database error during verification or creation: {db_error}")

async def fetch_with_retry(session, url):
    """Fetch URL with retries on rate limits."""
    while True:
        async with session.get(url, headers=HEADERS) as response:
            if response.status == 403:  # Rate limit exceeded
                reset_time = int(response.headers.get("X-RateLimit-Reset", time.time()))
                wait_time = max(0, reset_time - time.time())
                print(f"Rate limit exceeded. Waiting {wait_time} seconds.")
                await asyncio.sleep(wait_time)
                continue  # Retry after waiting
            response.raise_for_status()
            return await response.json()


async def fetch_repo_contents(session, repo_name):
    """Fetch the contents of a repository, including sub-folders."""
    repo_url = f"https://api.github.com/repos/{GITHUB_OWNER}/{repo_name}/contents"

    async def search_contents(url):
        """Recursive helper function to search for files in subdirectories."""
        try:
            contents = await fetch_with_retry(session, url)
            for item in contents:
                if item["type"] == "file" and item["name"] in REQUIRED_FILES:
                    # If a required file is found, return True
                    return True
                elif item["type"] == "dir":
                    # If it's a directory, recursively search it
                    sub_url = item["url"]
                    found = await search_contents(sub_url)
                    if found:
                        return True
        except Exception as e:
            print(f"Error searching contents at {url}: {e}")
        return False

    try:
        # Start searching from the root of the repository
        found_required_file = await search_contents(repo_url)
        if found_required_file:
            return repo_name
    except Exception as e:
        print(f"Error fetching contents for {repo_name}: {e}")
    return None


async def list_repositories():
    """List repositories from GitHub and filter based on required files."""
    all_repos = []
    page = 1
    per_page = 30

    async with aiohttp.ClientSession() as session:
        while True:
            paginated_url = f"https://api.github.com/users/{GITHUB_OWNER}/repos?page={page}&per_page={per_page}"
            repos = await fetch_with_retry(session, paginated_url)

            if not repos:  # No more pages
                break

            tasks = [fetch_repo_contents(session, repo["name"]) for repo in repos]
            filtered_repos = await asyncio.gather(*tasks)
            all_repos.extend(filter(None, filtered_repos))

            # Log the completion of scanning for the current page
            print(f"Scanned so far {page} pages , found {len(all_repos)} repositories with required files")

            page += 1

    return all_repos


def save_sbom_to_database(github_owner, repo_name, sbom):
    """Save SBOM data to PostgreSQL database.
        if your not allowing duplicate repos use the below line after VALUES

    	ON CONFLICT (reponame) DO NOTHING
    """
    query = """
        INSERT INTO sbom_data (repo_owner, reponame, sbom)
        VALUES (%s, %s, %s)
        RETURNING id;
    """
    try:
        with psycopg2.connect(DB_CONNECTION) as conn:
            with conn.cursor() as cursor:
                # Convert Python dict to JSON string
                sbom_json = json.dumps(sbom)

                # Execute the query with the JSON string
                cursor.execute(query, (github_owner, repo_name, sbom_json))
                sbom_id = cursor.fetchone()
                if sbom_id:
                    print(f"SBOM stored in the database with ID: {sbom_id[0]}")
    except psycopg2.Error as db_error:
        print(f"Database error: {db_error}")


def fetch_sbom(repo_name):
    """Fetch SBOM for a given repository."""
    url = f"{BASE_URL}{GITHUB_OWNER}/{repo_name}/dependency-graph/sbom"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        sbom_data = response.json()
        save_sbom_to_database(GITHUB_OWNER, repo_name, sbom_data)
    except requests.exceptions.RequestException as error:
        print(f"SBOM Graph not available for {repo_name}")


def process_repositories(repositories):
    """Fetch SBOMs for repositories concurrently."""
    with ThreadPoolExecutor() as executor:
        executor.map(fetch_sbom, repositories)

def check_rate_limit():
    """Fetch and display the remaining rate limit from GitHub."""
    url = "https://api.github.com/rate_limit"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        rate_limit_data = response.json()

        limit = rate_limit_data['rate']['limit']
        remaining = rate_limit_data['rate']['remaining']
        reset_time = int(rate_limit_data['rate']['reset'])
        reset_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(reset_time))

        print("\nGitHub API Rate Limit Status on your account:")
        print(f"Total Allowed Requests (per hour): {limit}")
        print(f"Remaining Requests: {remaining}")
        print(f"Rate Limit Resets At: {reset_time_str}")
        return limit, remaining, reset_time
    except requests.exceptions.RequestException as error:
        print(f"Error checking rate limit: {error}")
        return None, None, None

if __name__ == "__main__":
    print(f"\nI'm scanning only publicly available repos from the user {GITHUB_OWNER}.\n\nCurrently, I'm searching only for {REQUIRED_FILES} in the repositories.\n")

    try:
        print("\nVerifying database and table...")
        verify_or_create_database_and_table()

        print("\nScanning anf Fetching repositories...")
        repos = asyncio.run(list_repositories())
        
        if repos:
            # print list of repositories
            print(f"\nList of repos found in {GITHUB_OWNER} with {REQUIRED_FILES}:\n")
            # Create a list of rows for the table
            table_data = [[index + 1, repo] for index, repo in enumerate(repos)]

            # Print the table with headers
            print(tabulate(table_data, headers=["Index", "Repository Name"], tablefmt="grid"))

            print("\nProcessing repositories...\n")
            process_repositories(repos)
        else:
            print("\nNo repositories found with the required files.")
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # Check and log the remaining rate limit
        print("\nChecking remaining rate limit...")
        check_rate_limit() 
