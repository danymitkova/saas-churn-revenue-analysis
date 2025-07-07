import pandas as pd
def test_customer_ids_unique():
    df = pd.read_csv("data/raw/customers.csv")
    assert df["customer_id"].is_unique
