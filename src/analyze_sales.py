from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / 'data' / 'sales.csv', parse_dates=['order_date'])
df['revenue'] = df['quantity'] * df['unit_price']
out = ROOT / 'outputs'; out.mkdir(exist_ok=True)
monthly = df.assign(month=df['order_date'].dt.to_period('M').astype(str)).groupby('month', as_index=False)['revenue'].sum()
products = df.groupby('product', as_index=False)['revenue'].sum().sort_values('revenue', ascending=False)
regions = df.groupby('region', as_index=False)['revenue'].sum().sort_values('revenue', ascending=False)
monthly.to_csv(out / 'monthly_revenue.csv', index=False); products.to_csv(out / 'product_revenue.csv', index=False); regions.to_csv(out / 'regional_revenue.csv', index=False)
ax = monthly.plot(x='month', y='revenue', kind='line', marker='o', legend=False, title='Monthly Revenue')
ax.set_xlabel('Month'); ax.set_ylabel('Revenue'); plt.xticks(rotation=45, ha='right'); plt.tight_layout(); plt.savefig(out / 'monthly_revenue.png', dpi=160)
print('Rows:', len(df)); print('Total revenue:', round(df['revenue'].sum(), 2)); print('Outputs:', out)
