SELECT
    COUNT(DISTINCT order_id) AS order_count,
    SUM(amount) AS total_revenue,
    SUM(amount) / COUNT(DISTINCT order_id) AS AOV
FROM sales;