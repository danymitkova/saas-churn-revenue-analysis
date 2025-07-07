
# SaaS Churn & Revenue Impact Analysis

**Goal:** Predict customer churn for a subscription-based SaaS product and quantify the potential revenue impact of churn reduction strategies.

## Structure
| Folder | Contents |
|--------|----------|
| `data/raw` | Synthetic CSV datasets (`customers`, `events`, `subscriptions`) |
| `notebooks` | `churn_analysis.ipynb` — EDA, feature engineering, model training (logistic regression) |
| `sql` | `aggregations.sql` — example SQL for staging & aggregations |
| `dbt_demo_project` | Minimal dbt skeleton (`dbt_project.yml`, `models/`) |

## Quickstart
```bash
pip install -r requirements.txt
jupyter notebook notebooks/churn_analysis.ipynb
```

*Python ≥3.9 required.*
