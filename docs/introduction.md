# Introduction

This Python script automates the process of fetching Software Bill of Materials (SBOM) data for repositories from GitHub, storing the data in a PostgreSQL database, and handling rate limits effectively.

### Key Features
- Fetch SBOM for repositories containing `package.json` or `requirements.txt`.
- Store SBOM data in a PostgreSQL database for analysis.
- Handles GitHub API rate limits with retries.
- Uses asynchronous programming for efficient GitHub API interaction.