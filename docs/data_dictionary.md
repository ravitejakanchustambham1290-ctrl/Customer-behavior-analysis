# Data Dictionary

The source dataset contains **3,900 customer records and 18 original attributes**. The following fields are retained or derived for analysis.

| Field | Type | Description |
|---|---|---|
| `customer_id` | integer | Customer identifier |
| `age` | integer | Customer age |
| `gender` | categorical | Customer gender |
| `item_purchased` | categorical | Purchased product |
| `category` | categorical | Product category |
| `purchase_amount` | numeric | Purchase value in USD |
| `location` | categorical | Customer location |
| `size` | categorical | Purchased item size |
| `color` | categorical | Purchased item color |
| `season` | categorical | Season associated with purchase |
| `review_rating` | numeric | Product/customer review rating |
| `subscription_status` | categorical | Subscription status |
| `shipping_type` | categorical | Shipping method |
| `discount_applied` | categorical | Whether a discount was applied |
| `previous_purchases` | integer | Number of previous purchases |
| `payment_method` | categorical | Payment method |
| `frequency_of_purchases` | categorical | Purchase frequency label |
| `age_group` | categorical | Engineered quartile-based age segment |
| `purchase_frequency_days` | integer | Engineered approximate purchase interval in days |

`promo_code_used` is intentionally removed after validating that it duplicates `discount_applied` in the source data.
