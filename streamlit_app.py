import streamlit as st, pandas as pd
cust = pd.read_csv("data/raw/customers.csv", parse_dates=["signup_date"])
subs = pd.read_csv("data/raw/subscriptions.csv", parse_dates=["billing_date"])
st.title("📊 SaaS Churn & Revenue Dashboard")
st.metric("Overall churn", f"{cust['is_churned'].mean():.2%}")
st.line_chart(
    subs.groupby(subs["billing_date"].str[:7])["amount_usd"].sum()
)
