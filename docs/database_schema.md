# Database Schema

The script uses a PostgreSQL database to store SBOM data.

## Table: `sbom_data`
| Column Name  | Data Type        | Description                     |
|--------------|------------------|---------------------------------|
| `id`         | SERIAL           | Primary key                    |
| `reponame`   | VARCHAR(500)     | Name of the GitHub repository  |
| `sbom`       | JSONB            | SBOM data in JSON format       |
| `created_at` | TIMESTAMP        | Timestamp when the record was created |


### SQL Query to Create Table
```sql
CREATE TABLE sbom_data (
    id SERIAL PRIMARY KEY,
    reponame VARCHAR(500) NOT NULL,
    sbom JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

