# Sales Data Analysis Dashboard

A practical sales analytics workflow combining SQL aggregation, Python analysis and a Power BI dashboard guide.

## Included
- Synthetic order-line sample data in `data/sales.csv`
- SQL queries for revenue, monthly trends, products and regions
- Python script that exports summary tables and a monthly revenue chart
- Power BI setup guide

## Run
```bash
pip install -r requirements.txt
python src/analyze_sales.py
```
Import the CSV into a SQL table named `sales` to run `sql/analysis.sql`. Use `docs/power-bi-guide.md` to build the report. The data is synthetic; add conclusions only after running the analysis.
