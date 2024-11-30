# GitHub APIs Used

The script interacts with the following GitHub API endpoints:

## 1. List Repositories

- **Endpoint**: `GET /users/{GITHUB_OWNER}/repos`
- **Purpose**: Fetch all repositories owned by the user or organization.
- **Example**:
  - `curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/users/YOUR_USERNAME/repos`

## 2. Repository Contents

- Endpoint: `GET /repos/{GITHUB_OWNER}/{repo_name}/contents`
- Purpose: Fetch the contents of a specific repository to check for `package.json` or `requirements.txt`.

## 3. SBOM Data

- Endpoint: `GET /repos/{GITHUB_OWNER}/{repo_name}/dependency-graph/sbom`
- Purpose: Fetch the SBOM data for a specific repository.

## 4. Rate Limit

- Endpoint: `GET /rate_limit`
- Purpose: Check the remaining API request limit for the current GitHub token.


---
[Previous: APIs](apis.md) | [Next: Database](database_schema.md)