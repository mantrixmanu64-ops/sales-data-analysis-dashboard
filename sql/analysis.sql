-- Load data into a table named sales first.
-- Expected: order_id, order_date, region, product, category, quantity, unit_price, customer_id
SELECT COUNT(DISTINCT order_id) AS orders, COUNT(DISTINCT customer_id) AS customers, SUM(quantity * unit_price) AS revenue, SUM(quantity) AS units_sold FROM sales;
SELECT DATE_TRUNC('month', order_date) AS sales_month, SUM(quantity * unit_price) AS revenue FROM sales GROUP BY 1 ORDER BY 1;
SELECT product, SUM(quantity * unit_price) AS revenue FROM sales GROUP BY product ORDER BY revenue DESC;
SELECT region, SUM(quantity * unit_price) AS revenue FROM sales GROUP BY region ORDER BY revenue DESC;
