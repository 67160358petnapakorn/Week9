SELECT
    SUM(amount) AS total_revenue,
    AVG(amount) AS mean_line_amount,
    COUNT(*) AS line_count
FROM sales;