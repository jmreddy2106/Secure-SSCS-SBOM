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

---
<!-- [Previous: APIs](api.md) | [Next: Error Handling](error_handling.md) -->