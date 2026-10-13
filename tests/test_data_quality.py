
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "clean_transactions.csv"


def test_clean_transactions_file_exists():
    assert OUTPUT_FILE.exists(), "Clean transactions file is missing"


def test_clean_transactions_not_empty():
    df = pd.read_csv(OUTPUT_FILE)
    assert not df.empty, "Clean transactions file is empty"


def test_transaction_ids_are_unique():
    df = pd.read_csv(OUTPUT_FILE)
    assert df["transaction_id"].is_unique, "Duplicate transaction IDs found"


def test_transaction_amounts_are_positive():
    df = pd.read_csv(OUTPUT_FILE)
    assert (df["amount"] > 0).all(), "Invalid transaction amounts found"
