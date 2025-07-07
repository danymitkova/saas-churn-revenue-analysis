import pandas as pd
from pathlib import Path

ROOT = Path(__file__).parents[1]           # коренът на репото
DATA = ROOT / "saas_churn_project" / "data" / "raw"

def test_unique_customer_ids():
    df = pd.read_csv(DATA / "customers.csv")
    assert df["customer_id"].is_unique
