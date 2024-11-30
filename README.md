# Secure-SSCS-SBOM

### _Ensuring Trust and Transparency in Software Supply Chains_

---

## Documentation

For detailed instructions, please visit the complete [**Documentation**](https://jmreddy2106.github.io/Secure-SSCS-SBOM/).

---
### Background

- #### Software Bill of Materials (SBOM)

  - [CISA](https://www.cisa.gov/sbom)
  - [Blackduck](https://www.blackduck.com/blog/software-bill-of-materials-bom.html)
  - [GitLab](https://about.gitlab.com/blog/2022/10/25/the-ultimate-guide-to-sboms/)
  - [NTIA](https://www.ntia.gov/page/software-bill-materials)
  - [Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/generating-software-bills-of-materials-sboms-with-spdx-at-microsoft/)
  - [NIST](https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity/software-security-supply-chains-software-1)

- #### Software Supply Chain Security

  - [GitHub](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-supply-chain-security)
  - [Snyk](https://snyk.io/series/software-supply-chain-security/)
  - [Blackduck](https://www.blackduck.com/glossary/what-is-software-supply-chain-security.html)
  - [Google Cloud](https://cloud.google.com/software-supply-chain-security/docs/overview)
  - [NIST](https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity/software-supply-chain-security-guidance)

---

## **Overview**

Welcome to **Secure-SSCS-SBOM**, the cutting-edge solution to safeguard your software supply chain. By leveraging **Software Bill of Materials (SBOM)**, this project brings unprecedented transparency, accountability, and resilience to your software development lifecycle.

In an era where software dependencies grow increasingly complex, understanding "what’s in your software" is more critical than ever. **Secure-SSCS-SBOM** enables you to identify, monitor, and mitigate supply chain risks using industry-leading tools and best practices for SBOM management.

---

## **Key Features**

### :rocket: **End-to-End Supply Chain Security**

- Detect vulnerabilities across every component in your software stack.
- Secure third-party dependencies and open-source components.

### :mag: **Comprehensive SBOM Generation and Validation**

- Automatically generate SBOMs for your projects.
- Validate the integrity and authenticity of SBOM data.

### :link: **Seamless Integration**

- Integrate with CI/CD pipelines for automated security checks.
- Compatible with industry standards (SPDX, CycloneDX, etc.).

### :scroll: **Regulatory Compliance**

- Ensure compliance with modern regulations like **US Executive Order 14028** and **ISO 27001** standards.

### :star2: **Open and Extensible**

- Extensible architecture supports custom plugins and integrations.
- Open-source foundation for community contributions.

---

## **Why Secure-SSCS-SBOM?**

1. **Proactive Defense:** Stay ahead of emerging threats with real-time dependency insights.
2. **Transparency:** Know exactly what’s inside every release of your software.
3. **Efficiency:** Automate tedious tasks like vulnerability tracking and license auditing.
4. **Trust:** Foster customer confidence by demonstrating supply chain security practices.

---

## **Getting Started**

### **Prerequisites**

- **Git** (to clone the repository)
- **Docker** (optional, for containerized deployment)
- **Node.js**, **Python**, or your preferred SBOM-compatible environment

# Project Task List

## 🚀 Features

- [x] Generate SBOM from a project
- [x] Getting SBOM from GitHub
- [ ] Vulnerability Scanning
- [ ] Integration with CI/CD
- [ ] Compliance Reporting

## 🛠️ Development Tasks

- [x] Set up project repository
- [x] Write initial documentation
- [ ] Add automated tests
- [ ] Optimize performance
- [ ] Prepare dataset for Machine learning task
- [ ] Build and deploy ML models
- [ ] Develop Large-Language-Models (LLMs) using open-source libraries `Pytorch` or `tensorflow`

## 📦 Release Checklist

- [ ] Tag the release version
- [ ] Update `CHANGELOG.md`
- [ ] Deploy to production

## **Roadmap**

- [x] Fetching SBOM from GitHub API from popular programming languages (`Python` and `JavaScript`).
- [ ] Integration with SPDX and CycloneDX standards.
- [ ] Advanced analytics dashboard for supply chain insights.
- [ ] AI-driven risk prioritization and remediation.
- [ ] Community-contributed plugins and extensions.
- [ ] AI/ML integration to classify security levels



## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/secure-sscs-sbom.git
   cd secure-sscs-sbom

2. Download install the PostGreSQL database in your local machine

## Scan and Fetch SBOM from GitHub API

- Navigate to python folder and run the following command to fetch SBOM from GitHub API

3. The `fetch_github_sbom.py` script fetches the SBOM from `GitHub API`. To run it, first you need a [GitHub API token](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization) or `Personal Access Token (PAT)`. You can get it from your GitHub account settings. Then, you can run the script. 

:warning: **GitHub API Rate Limit:** Total number of requests is limited to **`5000`** per hour. To know more about GitHub API rate limits, please visit [GitHub API rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28)

## How to Create and Use a GitHub Personal Access Token (PAT)

1. Log in to your GitHub account and go to [Developer Settings](https://github.com/settings/tokens).
2. Click on **"Personal Access Tokens"** > **"Tokens (classic)"**.
3. Click the **"Generate new token"** button and choose **"Generate new token (classic)"**.
4. Add a description to your token (e.g., "My Personal Token").
5. Set the **expiration date** for your token (e.g., 30 days, 90 days, or no expiration).
6. Select the **scopes (permissions)** you need:
    - For repository access: Choose `repo` (full control of private repositories).
    - For working with Gists: Select `gist`.
    - Adjust scopes based on your requirements.
7. Click **"Generate token"**.
8. Copy the token displayed **immediately**. Once you navigate away, you won’t be able to see it again.

:warning: **Important:** Treat your PAT like a password. Do not share it or expose it in code or logs.

4. Create a `.env` file with your database credentials and other required configurations. You can use the following as a template.

    ```bash
    GITHUB_TOKEN=<your-github-token>      
    DB_CONNECTION=postgresql://<database_user>:<password>@<host/ip>:<port_number>/<Database_name>
    GITHUB_OWNER=<Git user>
5. Database setup: You can use the following SQL commands to create the required tables in your PostgreSQL database
    ```bash
    CREATE TABLE sbom_data (
        id SERIAL PRIMARY KEY,
        name VARCHAR(500) NOT NULL,
        sbom JSONB NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    )
6. Create a python virtual environment, activate virtual environment and install the required packages using pip. You can use the following command:

    ```bash
        python -m venv myvenv
        source myvenv/bin/activate (Linux/Ubuntu)
        myvenv\Scripts\activate (Windows)
        pip install -r requirements.txt
7. Run the `fetch_github_sbom.py` script to fetch the SBOM from GitHub API. The script will create a new database table if not exists and inserts the fetched SBOM data.


