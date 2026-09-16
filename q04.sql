SELECT
    month,
    full_date,
    SUM(amount) AS revenue
FROM sales
GROUP BY month, full_date
ORDER BY month, full_date;