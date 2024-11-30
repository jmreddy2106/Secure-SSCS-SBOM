# Installation

## Prerequisites
1. Python 3.x installed on your system.
2. PostgreSQL database instance available.
3. A GitHub personal access token with the required scopes (`repo` and `read:packages`).

## Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name/python

2. stall dependencies:
    ```bash
    pip install -r requirements.txt

3. Create a .env file in the root directory and configure it as shown in the Configuration section.
4. Run the following command to create the database schema and populate it with data:
    ```bash
        python sbom_fetcher.py
---

### `docs/configuration.md`
```markdown
# Configuration

The script uses environment variables to configure settings like the GitHub owner, token, and database connection string.

## `.env` File Setup
Create a `.env` file in the root directory of your project with the following variables:
```env
GITHUB_OWNER=your_github_username
GITHUB_TOKEN=your_github_personal_access_token
DB_CONNECTION=postgres://username:password@localhost:5432/mydatabase