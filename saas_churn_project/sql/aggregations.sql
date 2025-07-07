-- Example aggregation: monthly revenue and churn rate
WITH monthly_revenue AS (
    SELECT DATE_TRUNC('month', billing_date) AS month,
           SUM(amount_usd) AS revenue
    FROM subscriptions
    GROUP BY 1
),
monthly_churn AS (
    SELECT DATE_TRUNC('month', signup_date) + INTERVAL '12 month' AS month,
           COUNT(*) FILTER (WHERE is_churned = 1) AS churned
    FROM customers
    GROUP BY 1
)
SELECT r.month,
       r.revenue,
       c.churned
FROM monthly_revenue r
LEFT JOIN monthly_churn c USING (month)
ORDER BY r.month;
