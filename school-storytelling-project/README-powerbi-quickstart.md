# Power BI Quickstart for Financial data.csv

## Goal
Build a sales profitability dashboard from `Financial data.csv` using Glue/Athena or local import.

## Steps

1. Import Data
- Power BI Desktop → Get Data → CSV (or Amazon Athena) → select `Financial data.csv`.
- Ensure column types: `Date` = Date; numeric fields (Sales, COGS, Discounts, Profit, Units, Prices) = Decimal/Whole.

2. Create Date Table
- Modeling → New Table:
```
Dates = CALENDAR(MIN('Financial'[Date]), MAX('Financial'[Date]))
DateAttributes = ADDCOLUMNS(
    Dates,
    "Year", YEAR([Date]),
    "Month Number", MONTH([Date]),
    "Month Name", FORMAT([Date], "MMMM"),
    "Year-Month", FORMAT([Date], "YYYY-MM")
)
```
- Mark `Dates` as Date table; relate `'Financial'[Date]` → `Dates[Date]`.

3. Add Measures
- Copy contents from `powerbi-measures-dax.txt` into a Measures table.

4. Build Visuals
- Page 1 (KPIs): Cards for `Total Sales`, `Total Profit`, `Margin %`, `Discount %`.
- Page 1 (Trend): Line chart with `Dates[Year-Month]` → `Total Sales`, `Total Profit`.
- Page 2 (Margins): Line chart `Margin %` over `Dates[Year-Month]`; annotate dips.
- Page 2 (Discounts): Clustered column by `Financial[Discount Band]` with `Total Discounts` and `Margin %` (secondary axis via combo).
- Page 3 (Segments): Bar chart `Financial[Segment]` vs `Total Profit`; add `Margin %` in tooltip.
- Page 3 (Products): Combo chart `Financial[Product]` with columns `Total Sales` and line `Margin %`; add Pareto cumulative line (`Pareto Cum Profit`).
- Page 4 (Country): Bar or Filled Map `Financial[Country]` vs `Total Profit`, `Margin %`.
- Page 4 (Seasonality): Column chart `Dates[Month Number]` vs `Total Sales`, `Total Profit`.
- Page 5 (Elasticity): Scatter `Financial[Sale Price]` (X) vs `Financial[Units Sold]` (Y), size `Total Profit`, color `Financial[Product]`.

5. Slicers & Formatting
- Slicers: `Dates[Year]`, `Financial[Segment]`, `Financial[Country]`, `Financial[Product]`.
- Formats: Display units (Thousands/Millions), percentage formatting for `Margin %`, `Discount %`; enable data labels.

## Narrative Flow
- Hook: Profit can increase by optimizing discounts and focusing high-margin products.
- Findings: Trend → Drivers (Discounts, Segment/Product) → Geography → Seasonality → Elasticity → Pareto.
- Actions: Discount guardrails, focus segments/products, pricing experiments, geo playbooks.

## Tips
- Validate margins: `Total Sales - Total COGS - Total Discounts` vs `Total Profit` field.
- Use `MTD/YTD` measures for executive comparisons.
- Keep product count manageable (Top N filter) for clearer charts.
