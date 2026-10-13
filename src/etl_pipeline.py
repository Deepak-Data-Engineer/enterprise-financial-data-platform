
from pathlib import Path
import pandas as pd

# Resolve paths relative to the project directory.
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "transactions.csv"
OUTPUT_DIR = BASE_DIR / "data" / "processed"


def run_pipeline():
    print("Starting Financial Data ETL Pipeline...")

    # EXTRACT
    df = pd.read_csv(INPUT_FILE, dtype=str)
    print(f"Extracted {len(df)} transactions")

    # TRANSFORM
    required_columns = [
        "transaction_id", "customer_id", "account_id",
        "transaction_date", "transaction_type",
        "amount", "currency", "status"
    ]

    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    df = df.drop_duplicates(subset=["transaction_id"])

    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"], errors="coerce"
    )

    valid_statuses = {"COMPLETED", "PENDING", "FAILED"}
    valid_types = {"DEPOSIT", "WITHDRAWAL", "TRANSFER"}

    valid_mask = (
        df[required_columns].notna().all(axis=1)
        & (df["amount"] > 0)
        & df["status"].isin(valid_statuses)
        & df["transaction_type"].isin(valid_types)
        & df["currency"].eq("USD")
    )

    valid = df.loc[valid_mask].copy()
    rejected = df.loc[~valid_mask].copy()

    valid["transaction_date"] = valid[
        "transaction_date"
    ].dt.strftime("%Y-%m-%d")

    # Analytics: summarize completed transactions only.
    completed = valid[valid["status"] == "COMPLETED"]

    summary = (
        completed.groupby("customer_id", as_index=False)
        .agg(
            transaction_count=("transaction_id", "count"),
            total_transaction_amount=("amount", "sum")
        )
    )

    # LOAD
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    valid.to_csv(OUTPUT_DIR / "clean_transactions.csv", index=False)
    rejected.to_csv(OUTPUT_DIR / "rejected_transactions.csv", index=False)
    summary.to_csv(OUTPUT_DIR / "customer_summary.csv", index=False)

    print(f"Valid transactions: {len(valid)}")
    print(f"Rejected transactions: {len(rejected)}")
    print("ETL pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()
