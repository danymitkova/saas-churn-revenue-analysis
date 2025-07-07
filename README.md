# SaaS Churn & Revenue Impact Analysis
![CI](https://github.com/danymitkova/saas-churn-revenue-analysis/actions/workflows/ci.yml/badge.svg?branch=main)

End-to-end, **production-style** analytics project answering two questions:

1. **Which customers are likely to churn?**  
2. **How much revenue can we save by targeting them?**

The workflow mirrors what I did at Amazon, Salesforce & Databricks—data here is **synthetic** and privacy-safe.

---

## 📊 Interactive dashboard (Streamlit)

```bash
# run locally
pip install -r requirements.txt
streamlit run streamlit_app.py
Opens http://localhost:8501 with KPIs, revenue trend and churn-by-plan charts.

✅ Data-quality tests & CI
Tests live in tests/ and use pytest

Every push triggers GitHub Actions (see .github/workflows/ci.yml)

Badge at the top shows current status

🗂️ Project structure
pgsql
Copy
Edit
data/
└── raw/
    ├── customers.csv
    ├── events.csv
    └── subscriptions.csv
notebooks/
└── churn_analysis.ipynb
sql/
└── aggregations.sql
dbt_demo_project/
└── models/
    └── stg_customers.sql
streamlit_app.py
tests/
└── test_data_quality.py
🚀 Quick-start
bash
Copy
Edit
# optional venv
python -m venv venv && source venv/bin/activate

# install deps
pip install -r requirements.txt

# launch notebook
jupyter notebook notebooks/churn_analysis.ipynb
Python ≥ 3.9 required.

🏗️ Pipeline highlights
Layer	Tech	What happens
Raw → Staging	SQL (aggregations.sql)	Partitioned revenue & churn tables (lakehouse-ready)
Transformation	Jupyter + pandas	Feature engineering: event counts, one-hot plan encoding
Modelling	scikit-learn (LogReg)	AUC metric & classification report
Decision layer	matplotlib	📈 Curve “Revenue Saved vs Churn-probability Threshold”
dbt (optional)	dbt_demo_project	Shows where models would live in production

📊 Key results (synthetic)
AUC: ≈ 0.78 on hold-out set

Targeting customers with churn-probability > 0.4 could preserve ~ $120 K annual revenue



