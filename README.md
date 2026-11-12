# Sales Data Analysis Dashboard

A small end-to-end sales analytics project combining Python, SQL and a Power BI build guide. It turns sample order-line data into revenue summaries by month, product and region, with a chart for a quick trend review.

> **Dataset note:** The included sales records are synthetic and are intended for demonstration and practice.

## Project goals

- Calculate total revenue and summarize it by month, product and region.
- Use pandas to clean and aggregate the source CSV.
- Provide SQL examples for querying the same sales data.
- Export analysis-ready CSV files and a monthly revenue chart.
- Document how to turn the outputs into a Power BI report.

## Results from the committed run

- **Rows analyzed:** 12
- **Total revenue:** 4,653 dataset currency units
- **Highest-revenue month:** May 2025 (1,450)
- **Highest-revenue product:** Laptop (2,960)
- **Highest-revenue region:** East (1,530)

These are descriptive results from the included synthetic sample, not forecasts or claims about a real business.

## Monthly revenue

![Monthly revenue chart](outputs/monthly_revenue.png)

## Repository structure

```text
.
├── data/
│   └── sales.csv
├── docs/
│   └── power-bi-guide.md
├── outputs/
│   ├── monthly_revenue.csv
│   ├── monthly_revenue.png
│   ├── product_revenue.csv
│   └── regional_revenue.csv
├── sql/
│   └── analysis.sql
├── src/
│   └── analyze_sales.py
├── requirements.txt
└── README.md
```

## Getting started

### Requirements

- Python 3.10 or newer
- pip

### Run the Python analysis

```bash
python -m venv .venv
```

Activate the environment:

- **Windows Git Bash:** `source .venv/Scripts/activate`
- **Windows PowerShell:** `.\.venv\Scripts\Activate.ps1`
- **macOS / Linux:** `source .venv/bin/activate`

Then install and run:

```bash
pip install -r requirements.txt
python src/analyze_sales.py
```

The script creates the `outputs/` directory and writes the monthly, product and regional revenue summaries plus the monthly chart.

## SQL analysis

1. Create a database and import `data/sales.csv` into a table named `sales`.
2. Confirm the table column names match the queries.
3. Run the statements in [sql/analysis.sql](sql/analysis.sql) to explore total revenue and the monthly, product and regional breakdowns.

SQL is provided as an analysis example; adapt data types and import syntax to your database engine.

## Power BI

Follow [docs/power-bi-guide.md](docs/power-bi-guide.md) to import the source data or exported summaries and assemble a report. This repository currently contains the guide and Python-generated chart, **not a published interactive Power BI dashboard file**.

## Tools demonstrated

- Python and pandas
- SQL aggregation
- CSV-based data workflows
- Matplotlib visualization
- Power BI report planning
- Git and GitHub

## Limitations

- The sample contains only 12 synthetic rows.
- Findings describe this sample only and should not be generalized to an actual company.
- No live data connection, automated refresh or deployed dashboard is included.
