# Project Architecture

```text
                 ┌────────────────────┐
                 │ data/customer.csv  │
                 └──────────┬─────────┘
                            │
                            ▼
                 ┌────────────────────┐
                 │ Python / Pandas    │
                 │ EDA + Cleaning     │
                 │ Feature Engineering│
                 └──────────┬─────────┘
                            │
                            ▼
                 ┌────────────────────┐
                 │    PostgreSQL      │
                 │   customer table   │
                 └──────────┬─────────┘
                            │
                            ▼
                 ┌────────────────────┐
                 │ SQL Business Logic │
                 │ 10 analytical Qs   │
                 └──────────┬─────────┘
                            │
                            ▼
                 ┌────────────────────┐
                 │     Power BI       │
                 │ KPI + Interactive   │
                 │ Business Dashboard │
                 └────────────────────┘
```
