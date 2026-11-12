# Power BI Dashboard Guide

1. In Power BI Desktop, choose **Get Data → Text/CSV** and import `data/sales.csv`.
2. Set `order_date` to Date, `quantity` to Whole Number and `unit_price` to Decimal Number.
3. Create `Revenue = sales[quantity] * sales[unit_price]`.
4. Add KPI cards for revenue, orders, customers and units sold.
5. Add a monthly revenue line chart and product/region revenue bar charts.
6. Add date, region and category slicers.
7. Reconcile totals against `sql/analysis.sql`.

Suggested measures:
- Total Revenue = SUMX(sales, sales[quantity] * sales[unit_price])
- Orders = DISTINCTCOUNT(sales[order_id])
- Customers = DISTINCTCOUNT(sales[customer_id])
- Units Sold = SUM(sales[quantity])
