

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

# -----------------------------
# Order Items & Revenue Analysis
# -----------------------------

order_items= pd.read_csv("data/raw/olist_order_items_dataset.csv")
print(order_items.columns)

# Calculate total product revenue for each order
order_revenue=(
    order_items.groupby("order_id").agg(
        order_revenue=("price","sum")
    ).reset_index()
)
# Sort orders by revenue from highest to lowest
print(
    order_revenue.sort_values("order_revenue", ascending=False)
)

# Merge order revenue with order information
orders_revenue = pd.merge(
    orders,
    order_revenue,
    on="order_id",
    how="inner"
)
print(orders_revenue.head(5))

# Calculate total revenue by month
orders_revenue["order_purchase_timestamp"]=pd.to_datetime(
    orders_revenue["order_purchase_timestamp"]
)
orders_revenue["order_month"] = (
    orders_revenue["order_purchase_timestamp"].dt.to_period("M")
)
# Calculate total revenue by month
monthly_revenue = (
    orders_revenue.groupby("order_month").agg(
        monthly_revenue=("order_revenue", "sum")
    ).reset_index()
)
print(monthly_revenue)

# Identify the top 5 months by total revenue
top5_revenue = monthly_revenue.sort_values("monthly_revenue", ascending=False)
print(top5_revenue.head(5))

# Calculate average revenue per order (AOV)
avg_order_value=order_revenue["order_revenue"].mean()
print(avg_order_value)

# Merge revenue data with customer location information
customers=pd.read_csv("data/raw/olist_customers_dataset.csv")
customer_revenue = pd.merge(
    orders_revenue,
    customers,
    on="customer_id",
    how="inner"
)
print(customer_revenue.head(5))

# Calculate total revenue by customer state
state_revenue =customer_revenue.groupby("customer_state").agg(
    state_revenue = ("order_revenue", "sum")
).reset_index()
print(state_revenue.sort_values("state_revenue",ascending=False).head(10))

# -----------------------------
# Business Insights
# -----------------------------

# 1. November 2017 had the highest monthly revenue,
#    reaching approximately 1.01 million.
#    Revenue also remained relatively high from January to May 2018.

# 2. The average order value (AOV) was approximately 137.75.

# 3. SP generated the highest total revenue among all customer states,
#    with approximately 5.20 million in revenue.



# -----------------------------
# Product & Category Analysis
# -----------------------------
products = pd.read_csv(
    "data/raw/olist_products_dataset.csv"
)
print(products.columns)
print(products.head())

product_item = pd.merge(
    order_items,
    products,
    on = "product_id",
    how = "inner"
)
print(product_item.head())

product_category_count = (product_item.groupby("product_category_name").agg(
    item_count = ("product_id", "count")
).reset_index())
print(product_category_count.sort_values("item_count", ascending=False).head(10))

# print(product_item.columns)

# Group by product category and calculate total revenue
category_revenue = (
    product_item.groupby("product_category_name")
    .agg(
        category_revenue = ("price", "sum")
    )
    .reset_index()
)
print(
    category_revenue
    .sort_values("category_revenue", ascending=False)
    .head(10)
)

# Merge product category sales count and revenue into one summary table
category_summary = pd.merge(
    product_category_count,
    category_revenue,
    on="product_category_name",
    how="inner"
)
print(category_summary.head())
# Calculate the average revenue generated per item for each product category
category_summary["avg_revenue_per_item"] = category_summary["category_revenue"] / category_summary["item_count"]
print(
    category_summary.sort_values("avg_revenue_per_item",ascending=False)
    .head(10)
)
# -----------------------------
# Business Insights
# -----------------------------

# 1. cama_mesa_banho sold the most items among all product categories.

# 2. beleza_saude generated the highest total revenue among all product categories.

# 3. pcs had the highest average revenue per item.