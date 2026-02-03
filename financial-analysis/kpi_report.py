import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Resolve paths relative to this script's directory for robustness
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, 'Financial data.csv')
FIG_DIR = os.path.join(SCRIPT_DIR, 'figures')
REPORT_PATH = os.path.join(SCRIPT_DIR, 'kpi-visuals.md')

os.makedirs(FIG_DIR, exist_ok=True)

# Load data
# Date parsing and types
_df = pd.read_csv(DATA_PATH)

# Guard against division by zero
_df['Units Sold'] = _df['Units Sold'].replace(0, pd.NA)

# Derived metrics
_df['Net Sales'] = _df['Sales']
_df['Gross Profit'] = _df['Sales'] - _df['COGS']
_df['Gross Margin %'] = (_df['Gross Profit'] / _df['Sales']).replace([pd.NA, pd.NaT], 0) * 100
_df['ASP'] = (_df['Net Sales'] / _df['Units Sold']).astype(float)
_df['Unit COGS'] = (_df['COGS'] / _df['Units Sold']).astype(float)

# Overall KPIs
overall = {
    'Total Sales': float(_df['Net Sales'].sum()),
    'Total COGS': float(_df['COGS'].sum()),
    'Total Profit': float(_df['Gross Profit'].sum()),
}
overall['Gross Margin %'] = (overall['Total Profit'] / overall['Total Sales']) * 100 if overall['Total Sales'] else 0.0

# Aggregations
by_country = _df.groupby('Country').agg(
    Sales=('Net Sales', 'sum'),
    COGS=('COGS', 'sum'),
    Profit=('Gross Profit', 'sum')
)
by_country['Gross Margin %'] = (by_country['Profit'] / by_country['Sales']) * 100

by_product = _df.groupby('Product').agg(
    Sales=('Net Sales', 'sum'),
    COGS=('COGS', 'sum'),
    Profit=('Gross Profit', 'sum'),
    Units=('Units Sold', 'sum')
)
by_product['Gross Margin %'] = (by_product['Profit'] / by_product['Sales']) * 100
by_product['ASP'] = by_product['Sales'] / by_product['Units']
by_product['Unit COGS'] = by_product['COGS'] / by_product['Units']

by_segment = _df.groupby('Segment').agg(
    Sales=('Net Sales', 'sum'),
    Profit=('Gross Profit', 'sum')
)
by_segment['Gross Margin %'] = (by_segment['Profit'] / by_segment['Sales']) * 100

by_discount = _df.groupby('Discount Band').agg(
    Sales=('Net Sales', 'sum'),
    Profit=('Gross Profit', 'sum')
)
by_discount['Gross Margin %'] = (by_discount['Profit'] / by_discount['Sales']) * 100

# Visualization helpers
sns.set(style='whitegrid')

def save_barplot(df, x_col, y_col, title, filename, rotate=False, top_n=None):
    d = df.copy()
    if top_n:
        d = d.sort_values(y_col, ascending=False).head(top_n)
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=d.index if x_col == 'index' else d[x_col], y=d[y_col], palette='Blues_r')
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    if rotate:
        plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    out = os.path.join(FIG_DIR, filename)
    plt.savefig(out)
    plt.close()
    return out

# Charts
figs = {}
figs['profit_by_product'] = save_barplot(by_product, 'index', 'Profit', 'Profit by Product', 'profit_by_product.png', rotate=True, top_n=12)
figs['profit_by_country'] = save_barplot(by_country, 'index', 'Profit', 'Profit by Country', 'profit_by_country.png', rotate=True)
figs['margin_by_segment'] = save_barplot(by_segment, 'index', 'Gross Margin %', 'Gross Margin % by Segment', 'margin_by_segment.png', rotate=True)
figs['asp_top_products'] = save_barplot(by_product, 'index', 'ASP', 'ASP (Average Selling Price) – Top 12 Products', 'asp_top_products.png', rotate=True, top_n=12)
figs['discount_margin'] = save_barplot(by_discount, 'index', 'Gross Margin %', 'Gross Margin % by Discount Band', 'discount_margin.png', rotate=True)

# Scatter: ASP vs Unit COGS (by product)
plt.figure(figsize=(9, 6))
pp = by_product.dropna(subset=['ASP', 'Unit COGS'])
ax = sns.scatterplot(x=pp['Unit COGS'], y=pp['ASP'])
for label in pp.index:
    ax.annotate(label, (pp.loc[label, 'Unit COGS'], pp.loc[label, 'ASP']), fontsize=8, alpha=0.7)
plt.title('ASP vs Unit COGS (per Product)')
plt.xlabel('Unit COGS')
plt.ylabel('ASP')
plt.tight_layout()
scatter_path = os.path.join(FIG_DIR, 'asp_vs_unitcogs.png')
plt.savefig(scatter_path)
plt.close()
figs['asp_vs_unitcogs'] = scatter_path

# Write markdown report with key tables and images
lines = []
lines.append('# KPI Visuals Report\n')
lines.append('## Overall KPIs\n')
lines.append(f"- Total Sales: {overall['Total Sales']:.2f}\n")
lines.append(f"- Total COGS: {overall['Total COGS']:.2f}\n")
lines.append(f"- Total Profit: {overall['Total Profit']:.2f}\n")
lines.append(f"- Gross Margin %: {overall['Gross Margin %']:.2f}%\n")

lines.append('\n## Country Performance\n')
lines.append(f"![Profit by Country]({os.path.relpath(figs['profit_by_country'])})\n")

lines.append('\n## Product Performance\n')
lines.append(f"![Profit by Product]({os.path.relpath(figs['profit_by_product'])})\n")
lines.append(f"![ASP – Top Products]({os.path.relpath(figs['asp_top_products'])})\n")
lines.append(f"![ASP vs Unit COGS]({os.path.relpath(figs['asp_vs_unitcogs'])})\n")

lines.append('\n## Segment & Discount\n')
lines.append(f"![Gross Margin % by Segment]({os.path.relpath(figs['margin_by_segment'])})\n")
lines.append(f"![Gross Margin % by Discount Band]({os.path.relpath(figs['discount_margin'])})\n")

with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Report written to:', REPORT_PATH)
print('Figures saved to:', FIG_DIR)
