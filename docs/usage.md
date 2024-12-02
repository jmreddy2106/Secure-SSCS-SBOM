## Running the Script

1. Ensure your `.env` file is configured correctly.
<br><br> 

2. Run the script:
```bash
   python python/sbom_fetcher.py
```

## Script Workflow

1. Verifies or creates the required PostgreSQL table (`sbom_data`).
<br><br> 
2. Scans the repositories of the specified GitHub owner for the required files (`package.json`, `requirements.txt`).
<br><br> 
3. Fetches SBOM data for repositories containing the required files.
<br><br> 
4. Saves the SBOM data in the PostgreSQL database.
<br><br> 

## Expected Output

- Logs indicating progress, such as:
    - "Scanning completed for page X"
    - "SBOM stored in the database with ID: X"
<br><br> 
- Remaining rate limit at the end of the script.

---

<!-- [Previous: Configuration](configuration.md) | [Next: APIs](api.md) -->
