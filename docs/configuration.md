# Configurations

The script uses environment variables to configure settings like the GitHub owner, token, and database connection string.

# `.env` File Setup
Create a `.env` file in the root directory of your project with the following variables: 
```bash
GITHUB_OWNER=your_github_username
GITHUB_TOKEN=your_github_personal_access_token
DB_CONNECTION=postgres://username:password@localhost:5432/mydatabase
```

# Explanation of Variables

```bash
GITHUB_OWNER: GitHub username or organization name.
GITHUB_TOKEN: Personal access token for authentication with GitHub.
DB_CONNECTION: PostgreSQL connection string, including credentials.

```

---
<!-- [Previous: Installation](installation.md) | [Next: Usage](usage.md) -->