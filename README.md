# Enterprise Financial Data Platform

### End-to-End Banking Data Engineering & Analytics Project

An independently developed, banking-inspired data engineering project demonstrating financial data ingestion, ETL processing, data quality validation, SQL analytics, automated testing, and pipeline execution using GitHub Actions.

> **Disclaimer:** This is an independent portfolio project built using sample financial data. It is not an official First United Bank system and does not contain confidential banking information or proprietary employer code.

---

## Project Overview

The Enterprise Financial Data Platform simulates an end-to-end financial data processing workflow.

The platform ingests sample banking transactions, applies data validation and transformation rules, separates valid and rejected records, and generates reporting-ready datasets for financial analytics.

It demonstrates practical data engineering concepts, including reproducible ETL pipelines, SQL-based reporting, automated data quality testing, and CI workflow execution.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas |
| Analytics | SQL |
| Database | SQLite |
| Data Quality | Python Validation, pytest |
| Automation | GitHub Actions |
| Version Control | Git, GitHub |
| Data Formats | CSV |

## Architecture
**[View Interactive Architecture Diagram](docs/architecture.md)**

```text
Sample Banking Transactions (CSV)
                 |
                 v
         Python ETL Pipeline
                 |
                 v
       Data Quality Validation
                 |
          +------+------+
          |             |
          v             v
   Clean Transactions   Rejected Records
          |
          +-------------------+
          |                   |
          v                   v
   Customer Summaries    SQLite Database
                              |
                              v
                         SQL Analytics
                              |
                              v
                      Five CSV Reports

GitHub Actions Workflow
    |
    +-- Run Python ETL
    +-- Run SQL Analytics
    +-- Run pytest Data Quality Tests
    +-- Upload Generated Artifacts
```

## Key Features

### 1. Financial Data Ingestion

- Reads sample banking transaction records from CSV files.
- Provides a reproducible input dataset for ETL processing.
- Supports local execution and GitHub Actions workflows.

### 2. Python ETL Processing

- Processes transaction records using Python and Pandas.
- Applies validation and transformation logic.
- Produces cleaned transaction datasets.
- Separates rejected transactions for inspection.

### 3. Data Quality Validation

- Checks transaction records against validation rules.
- Separates accepted and rejected records.
- Supports reliable downstream financial reporting.

### 4. Customer-Level Reporting

- Generates customer transaction summaries.
- Produces structured outputs for further analysis.

### 5. SQL Analytics

Uses SQLite and SQL to generate five analytical reports:

1. Completed transaction summaries by customer
2. Transaction volume by type
3. Daily transaction trends
4. Transaction status monitoring
5. Customer transaction ranking

### 6. Automated Data Quality Testing

Uses **pytest** to verify processed transaction data.

The four automated tests confirm:

- The cleaned transactions file exists.
- The cleaned transactions dataset is not empty.
- Transaction IDs are unique.
- Transaction amounts are positive.

**Verified Test Results: 4 passed, 0 failed.**

These tests execute within the GitHub Actions workflow.

### 7. GitHub Actions Automation

The workflow supports manually triggered execution and performs the following steps:

1. Downloads repository files.
2. Configures the Python environment.
3. Installs project dependencies.
4. Runs the Python ETL pipeline.
5. Executes SQL analytics.
6. Runs automated data quality tests.
7. Uploads generated outputs as downloadable artifacts.

## Project Structure

```text
enterprise-financial-data-platform/
|
|-- .github/
|   |-- workflows/
|       |-- run-etl.yml
|
|-- data/
|   |-- transactions.csv
|   |-- processed/              # Generated during execution
|
|-- sql/
|   |-- financial_analytics.sql
|
|-- src/
|   |-- etl_pipeline.py
|   |-- run_sql_analytics.py
|
|-- tests/
|   |-- test_data_quality.py
|
|-- requirements.txt
|-- README.md
```

## How to Run

### Option 1: Run Locally

**Step 1 — Clone the repository**

```bash
git clone https://github.com/Deepak-Data-Engineer/enterprise-financial-data-platform.git
cd enterprise-financial-data-platform
```

**Step 2 — Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**Step 3 — Run the ETL pipeline**

```bash
python src/etl_pipeline.py
```

**Step 4 — Run SQL analytics**

```bash
python src/run_sql_analytics.py
```

**Step 5 — Execute automated tests**

```bash
python -m pytest tests/ -v
```

### Option 2: Run with GitHub Actions

1. Open the repository's **Actions** tab.
2. Select **Run Financial ETL Pipeline**.
3. Click **Run workflow**.
4. Select the `main` branch.
5. Start the workflow and wait for completion.
6. Open the completed workflow run.
7. Download the `banking-etl-results` artifact.

## Generated Outputs

The pipeline produces:

| Output | Description |
|---|---|
| `clean_transactions.csv` | Transactions that passed validation |
| `rejected_transactions.csv` | Transactions that failed validation |
| `customer_summary.csv` | Customer-level transaction summaries |
| `sql_reports/` | Five SQL analytics reports |

Generated files are saved under `data/processed/` during execution and are available through GitHub Actions artifacts.

## Workflow Validation

The GitHub Actions workflow has been successfully executed.

**Verified execution:**

- Workflow: Run Financial ETL Pipeline #3
- Status: Success
- ETL execution: Successful
- SQL analytics: Successful
- Automated tests: 4 passed
- Output artifacts: Generated successfully

The automated test suite verifies the existence, completeness, uniqueness, and positive transaction amounts of the cleaned dataset.

## Skills Demonstrated

- End-to-end ETL pipeline development
- Python and Pandas data processing
- SQL analytics and financial reporting
- SQLite database operations
- Data quality validation
- Automated testing using pytest
- GitHub Actions workflow automation
- Version control and project documentation
- Reproducible data engineering workflows

## Future Enhancements

Potential future improvements include:

- Cloud storage integration using Azure or AWS
- Workflow orchestration using Apache Airflow
- Scalable data processing with Apache Spark
- Additional automated data quality rules
- Enhanced monitoring and logging
- Larger synthetic financial datasets

---

**Project Type:** Independent data engineering portfolio project

**Domain:** Banking and Financial Services

**Data:** Sample financial transaction records

**Purpose:** Demonstrate practical data engineering, analytics, and automated testing capabilities.
