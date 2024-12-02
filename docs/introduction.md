# Introduction

This Python script automates the process of fetching Software Bill of Materials (SBOM) data for repositories from GitHub, storing the data in a PostgreSQL database, and handling rate limits effectively.




### Key Features

- Fetch SBOM for repositories containing `package.json` or `requirements.txt`.
<br><br> 
- Store SBOM data in a PostgreSQL database for analysis.
<br><br> 
- Handles GitHub API rate limits with retries.
<br><br> 
- Uses asynchronous programming for efficient GitHub API interaction.

---
<!-- [Previous: Home](index.md) | [Next: Installations](installation.md) -->