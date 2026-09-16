SELECT
    product_name,
    SUM(quantity) AS total_quantity,
    SUM(amount) AS revenue
FROM sales
GROUP BY product_name
ORDER BY revenue DESC;