# Methodology

## Data quality

- Loaded the raw CSV with Pandas.
- Inspected dimensions, data types, descriptive statistics, and missing values.
- Found missing `review_rating` values and imputed them using the median review rating within each product category.

## Feature engineering

- Standardized column names to `snake_case` for SQL/Python interoperability.
- Renamed `purchase_amount_(usd)` to `purchase_amount`.
- Created four quartile-based age groups: `young adult`, `adult`, `middle age`, and `senior`.
- Converted purchase-frequency labels to approximate day intervals.
- Validated that `promo_code_used` matches `discount_applied` before removing the redundant field.

## SQL analytics

The SQL layer answers ten business questions covering revenue, discounts, product ratings, shipping, subscription behavior, loyalty segmentation, product ranking, repeat buyers, and age-group revenue.

## BI layer

The supplied Power BI dashboard presents KPI cards, slicers, category performance, subscription mix, seasonal distribution, age-group revenue, and purchase-frequency analysis. The dashboard preview is stored in `dashboard/dashboard_preview.pdf`.
