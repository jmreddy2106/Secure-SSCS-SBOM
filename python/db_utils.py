import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path

# Determine the project's root directory
ROOT_DIR = Path(__file__).resolve().parent.parent

# Load the .env file from the root directory
load_dotenv(ROOT_DIR / '.env')


# Database connection string
DB_CONNECTION = os.getenv('DB_CONNECTION')  # PostgreSQL connection string

def verify_or_create_database_and_tables():
    """Verify and create necessary database tables."""
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
                sbom_table_exists = cursor.fetchone()[0]

                # Create the `sbom_data` table if it doesn't exist
                if not sbom_table_exists:
                    print("Table 'sbom_data' does not exist. Creating it now...")
                    cursor.execute("""
                        CREATE TABLE sbom_data (
                            id SERIAL PRIMARY KEY,
                            repo_owner VARCHAR(500) NOT NULL,
                            reponame VARCHAR(500) NOT NULL,
                            sbom JSONB NOT NULL,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        );
                    """)
                    print("Table 'sbom_data' created successfully.")
                else:
                    print("Table 'sbom_data' already exists.")

                # Check if the `vulnerabilities` table exists
                cursor.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE table_name = 'vulnerabilities'
                    );
                """)
                vulnerabilities_table_exists = cursor.fetchone()[0]

                # Create the `vulnerabilities` table if it doesn't exist
                if not vulnerabilities_table_exists:
                    print("Table 'vulnerabilities' does not exist. Creating it now...")
                    cursor.execute("""
                        CREATE TABLE vulnerabilities (
                            id SERIAL PRIMARY KEY,
                            repo_name VARCHAR(500) NOT NULL,
                            package VARCHAR(255) NOT NULL,
                            version VARCHAR(50) NOT NULL,
                            ecosystem VARCHAR(50) NOT NULL,
                            vulnerability_id VARCHAR(500) NOT NULL,
                            severity_type VARCHAR(100) NOT NULL,
                            severity_score FLOAT NOT NULL,
                            severity_level VARCHAR(100) NOT NULL,
                            summary TEXT,
                            UNIQUE (repo_name, package, version, vulnerability_id)
                        );
                    """)
                    print("Table 'vulnerabilities' created successfully.")
                else:
                    print("Table 'vulnerabilities' already exists.")

    except psycopg2.Error as db_error:
        print(f"Database error during verification or creation: {db_error}")
        exit(1)  # Exit the script if there's a database error
