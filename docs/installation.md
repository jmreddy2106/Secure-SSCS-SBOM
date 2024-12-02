# Installation

## Prerequisites

1. Python 3.x installed on your system.
2. PostgreSQL database instance available.
3. A GitHub personal access token with the required scopes (`repo` and `read:packages`).

## Steps to Install

1. Clone the repository:
```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name/python`
```
<br><br> 
2. stall dependencies:
```bash
    pip install -r requirements.txt
```
<br><br> 
3. Create a `.env` file in the root directory and configure it as shown in the Configuration section.
<br><br> 
4. Run the following command to create the database schema and populate it with data:
```bash
    python sbom_fetcher.py
```

---

<!-- [Previous: Home](index.md) | [Next: Configuration](configuration.md) -->
