
from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "clean_transactions.csv"
SQL_FILE = BASE_DIR / "sql" / "financial_analytics.sql"
OUTPUT_DIR = BASE_DIR / "data" / "processed" / "sql_reports"


def run_sql_analytics():
    print("Starting SQL analytics...")

    # Load validated transactions from the ETL pipeline.
    df = pd.read_csv(INPUT_FILE)

    # Create an in-memory SQLite database.
    with sqlite3.connect(":memory:") as connection:
        df.to_sql(
            "clean_transactions",
            connection,
            index=False,
            if_exists="replace"
        )

        # Read the five SQL queries.
        sql_text = SQL_FILE.read_text(encoding="utf-8")
        queries = [
            query.strip()
            for query in sql_text.split(";")
            if query.strip()
        ]

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        for number, query in enumerate(queries, start=1):
            result = pd.read_sql_query(query, connection)

            output_file = OUTPUT_DIR / f"report_{number}.csv"
            result.to_csv(output_file, index=False)

            print(
                f"Report {number}: "
                f"{len(result)} rows saved"
            )

    print("SQL analytics completed successfully!")


if __name__ == "__main__":
    run_sql_analytics()
