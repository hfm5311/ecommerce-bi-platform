import pandas as pd


# Task 1: Analyze order status distribution
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

print(
    orders["order_status"]
    .value_counts()
    .sort_values(ascending=False)
)


# Task 2: Analyze monthly order volume
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

# Create a year-month column for monthly trend analysis
orders["order_month"] = (
    orders["order_purchase_timestamp"]
    .dt.to_period("M")
)

print(
    orders[
        ["order_purchase_timestamp", "order_month"]
    ].head()
)

# Count the number of orders in each month
monthly_orders = (
    orders.groupby("order_month")
    .agg(
        order_count=("order_id", "count")
    )
    .reset_index()
)

print(monthly_orders)


# Task 3: Analyze payment methods
payments = pd.read_csv(
    "data/raw/olist_order_payments_dataset.csv"
)

print(payments.columns)

# Calculate payment record count and average payment value
# for each payment type
payment_summary = (
    payments.groupby("payment_type")
    .agg(
        payment_count=("payment_type", "count"),
        avg_payment=("payment_value", "mean")
    )
    .reset_index()
)

# Sort payment methods by usage frequency
print(
    payment_summary.sort_values(
        "payment_count",
        ascending=False
    )
)