# Database Schema

The script uses a PostgreSQL database to store SBOM data.

## Table: `sbom_data`

| Column Name  | Data Type        | Description                     |
|--------------|------------------|---------------------------------|
| `id`         | SERIAL           | Primary key                    |
| `repo_owner` | VARCHAR(500)     | Repository owner's GitHub handle|
| `reponame`   | VARCHAR(500)     | Name of the GitHub repository  |
| `sbom`       | JSONB            | SBOM data in JSON format       |
| `created_at` | TIMESTAMP        | Timestamp when the record was created |


### SQL Query to Create Table

```sql
CREATE TABLE sbom_data (
    id SERIAL PRIMARY KEY,
    repo_owner VARCHAR(500) NOT NULL,
    reponame VARCHAR(500) NOT NULL,
    sbom JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
```

### Table: `Vulnerabilities`

The `vulnerabilities` table stores information about vulnerabilities detected in specific repositories and their associated packages. Each column in the table is described below:

| Column Name         | Data Type          | Constraints         | Description                                                                 |
|---------------------|--------------------|---------------------|-----------------------------------------------------------------------------|
| `id`                | `SERIAL`          | `PRIMARY KEY`       | A unique identifier for each record in the table. Automatically generated. |
| `repo_name`         | `VARCHAR(255)`    | `NOT NULL`          | The name of the repository where the vulnerability was detected.           |
| `package`           | `VARCHAR(255)`    | `NOT NULL`          | The name of the package in which the vulnerability exists.                 |
| `version`           | `VARCHAR(50)`     | `NOT NULL`          | The version of the package where the vulnerability was identified.         |
| `ecosystem`         | `VARCHAR(50)`     | `NOT NULL`          | The ecosystem or package manager (e.g., npm, PyPI, Maven) of the package.  |
| `vulnerability_id`  | `VARCHAR(100)`    | `NOT NULL`          | A unique identifier for the vulnerability (e.g., CVE ID).                  |
| `severity_type`     | `VARCHAR(50)`     | `NOT NULL`          | The type of severity (e.g., CVSS).                                         |
| `severity_score`    | `FLOAT`           | `NOT NULL`          | The numerical severity score (e.g., CVSS score).                           |
| `severity_level`    | `VARCHAR(20)`     | `NOT NULL`          | The categorized severity level (e.g., Low, Medium, High).                  |
| `summary`           | `TEXT`            |                     | A textual summary describing the vulnerability.                            |
| **Unique Constraint** |                  | `UNIQUE(repo_name, package, version, vulnerability_id)` | Ensures that no duplicate entries exist for the same package vulnerability within a repository. |

```sql
    CREATE TABLE vulnerabilities (
        id SERIAL PRIMARY KEY,
        repo_name VARCHAR(255) NOT NULL,
        package VARCHAR(255) NOT NULL,
        version VARCHAR(50) NOT NULL,
        ecosystem VARCHAR(50) NOT NULL,
        vulnerability_id VARCHAR(100) NOT NULL,
        severity_type VARCHAR(50) NOT NULL,
        severity_score FLOAT NOT NULL,
        severity_level VARCHAR(20) NOT NULL,
        summary TEXT,
        UNIQUE (repo_name, package, version, vulnerability_id)
    );
```

---
<!-- [Previous: APIs](api.md) | [Next: Error Handling](error_handling.md) -->