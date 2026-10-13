
# Enterprise Financial Data Platform

### End-to-End Banking Data Engineering & Analytics Project

An independently developed, banking-inspired data engineering project demonstrating financial data ingestion, ETL processing, data quality validation, SQL analytics, and automated pipeline execution.

> **Note:** This is a portfolio demonstration using sample data. It is not an official First United Bank system and contains no confidential banking information.

## Project Overview

This project simulates a financial data processing workflow in which transaction records are ingested, validated, transformed, and analyzed to produce reporting-ready datasets.

The goal is to demonstrate practical data engineering fundamentals using a reproducible pipeline.

## Technology Stack

- **Python** — ETL processing and automation
- **Pandas** — Data transformations and CSV processing
- **SQL** — Financial analytics and reporting
- **SQLite** — Lightweight analytical database
- **GitHub Actions** — Automated pipeline execution
- **Git and GitHub** — Version control and CI workflow management

## Architecture

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
       v
   SQLite Database
       |
       v
   SQL Analytics
       |
       v
  Five CSV Reports
```

## Key Features

### 1. Financial Data Ingestion
Reads sample transaction data from CSV files.

### 2. ETL Processing
Processes financial transaction records using Python and Pandas.

### 3. Data Quality Validation
Separates accepted transactions from records that fail validation.

### 4. Customer-Level Reporting
Produces customer transaction summaries.

### 5. SQL Analytics
Includes five analytical queries covering:

- Completed transaction summaries by customer
- Transaction volume by type
- Daily transaction trends
- Transaction status monitoring
- Customer transaction ranking

### 6. GitHub Actions Automation
Runs the Python ETL and SQL analytics scripts through a manually triggered GitHub Actions workflow.

## Project Structure

```text
enterprise-financial-data-platform/
|
|-- .github/workflows/run-etl.yml
|-- data/
|   |-- transactions.csv
|-- sql/
|   |-- financial_analytics.sql
|-- src/
|   |-- etl_pipeline.py
|   |-- run_sql_analytics.py
|-- requirements.txt
|-- README.md
```

Generated files are saved under `data/processed/` during execution.

## How to Run

### Run locally

1. Clone this repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the ETL pipeline:

```bash
python src/etl_pipeline.py
```

4. Run SQL analytics:

```bash
python src/run_sql_analytics.py
```

### Run using GitHub Actions

1. Open the **Actions** tab.
2. Select **Run Financial ETL Pipeline**.
3. Click **Run workflow**.
4. Wait for the workflow to complete.
5. Download the `banking-etl-results` artifact.

## Generated Outputs

The pipeline produces:

- `clean_transactions.csv`
- `rejected_transactions.csv`
- `customer_summary.csv`
- Five SQL analytics reports under `sql_reports/`

## Skills Demonstrated

Python ETL | Pandas | SQL | SQLite | Data Validation | Financial Data Processing | Workflow Automation | GitHub Actions

## Future Enhancements

Potential extensions include cloud storage integration, orchestration, automated testing, and scalable processing with Apache Spark.

---

**Project Type:** Independent portfolio project using sample financial data.
