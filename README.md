# SaaS Churn & Revenue Impact Analysis
![CI](https://github.com/danymitkova/saas-churn-revenue-analysis/actions/workflows/ci.yml/badge.svg)


An end-to-end, **production-style** analytics project that answers two business questions:

1. **Which customers are likely to churn?**  
2. **How much revenue can we save by targeting them?**

The project mirrors the workflow I used at Amazon, Salesforce, and Databricks—only the data here is fully **synthetic** and privacy-safe.

---
## 📊 Interactive dashboard (Streamlit)

Run locally:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
## ✅ Data-quality tests & CI

- Tests live in `tests/` and use **pytest**.  
- Every push triggers GitHub Actions (`.github/workflows/ci.yml`).  
- Badge at the top shows the current status.


## 🗂️ Project structure

saas-churn-revenue-analysis/
├── README.md
├── requirements.txt
├── data/
│ └── raw/
│ ├── customers.csv # sign-ups, plan, region, churn flag
│ ├── events.csv # behavioural events (login, feature_use…)
│ └── subscriptions.csv # monthly billing amounts
├── notebooks/
│ └── churn_analysis.ipynb # EDA → features → model → revenue curve
├── sql/
│ └── aggregations.sql # lakehouse staging + KPI example
└── dbt_demo_project/ # minimal dbt skeleton
├── dbt_project.yml
└── models/
└── stg_customers.sql

yaml
Copy
Edit

---

## 🚀 Quick-start

```bash
# Create a clean environment (optional)
python -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch the notebook
jupyter notebook notebooks/churn_analysis.ipynb
Python ≥ 3.9 required.

🏗️ Pipeline highlights
Layer	Tech used	What happens
Raw → Staging	SQL (aggregations.sql)	Partitioned revenue + churn tables (lakehouse-ready)
Transformation	Jupyter + pandas	Feature engineering: event counts, one-hot plan encoding
Modelling	scikit-learn (Logistic Regression)	AUC metric & classification report
Decision layer	matplotlib	📈 Curve: “Revenue Saved vs Churn-probability Threshold”
dbt (optional)	dbt_demo_project	Shows where models would live in production

📊 Key results (synthetic)
AUC: ≥ 0.78 on hold-out set

Targeting customers with churn-probability > 0.4 could preserve ≈ $120 K annual revenue (see notebook for methodology).

🔧 Extending the project
Swap the synthetic CSVs with your own data—column names are documented in each file.

Connect the dbt skeleton to Snowflake, BigQuery, or Databricks SQL to test in a real lakehouse.

Replace Logistic Regression with XGBoost or AutoML and compare the uplift curve.

