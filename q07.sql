SELECT
    province,
    SUM(amount) AS revenue
FROM sales
GROUP BY province
HAVING SUM(amount) > 500
ORDER BY revenue DESC;