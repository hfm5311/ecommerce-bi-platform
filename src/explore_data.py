import pandas as pd
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

print(orders.head(5))
print(orders.shape)
print(orders.columns)

orders.info()
missing_values = orders.isnull().sum()
print(missing_values)

print(orders["order_status"].value_counts())

print(
    orders.loc[
        orders["order_delivered_customer_date"].isnull(),
        "order_status"
    ].value_counts()
    
)

print(
    orders.loc[
        (orders["order_status"] == "delivered" )& (orders["order_delivered_customer_date"].isnull()),
        ["order_id", "order_status", "order_purchase_timestamp", "order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date"]
    ]
)

print(
    orders["order_id"].duplicated().sum()
)

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")
print(orders[date_columns].dtypes)

print(orders[date_columns].isnull().sum())

customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
print(customers.shape)
missing_values = customers.isnull().sum()
print(missing_values)

print(customers["customer_id"].duplicated().sum())
print(customers["customer_unique_id"].duplicated().sum())

order_items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
print(order_items.shape)
missing_values = order_items.isnull().sum()
print(missing_values)

print(
    order_items.duplicated(
        subset = ["order_id", "order_item_id"]
    ).sum()
)

payments = pd.read_csv("data/raw/olist_order_payments_dataset.csv")
print(payments.shape)
missing_values = payments.isnull().sum()
print(missing_values)
print(
    payments.duplicated(
        subset = ["order_id", "payment_sequential"]
    ).sum()
)

reviews = pd.read_csv("data/raw/olist_order_reviews_dataset.csv")
print(reviews.shape)
missing_values = reviews.isnull().sum()
print(missing_values)
print(reviews["review_id"].duplicated().sum())

duplicate_reviews = reviews[
    reviews["review_id"].duplicated(keep=False)
]

print(
    duplicate_reviews[
        ["review_id", "order_id", "review_score"]
    ].sort_values("review_id").head(20)
)

print(
    reviews.duplicated(
        subset = ["review_id", "order_id"]
    ).sum()
)

products = pd.read_csv("data/raw/olist_products_dataset.csv")
print(products.shape)
missing_values = products.isnull().sum()
print(missing_values)
print(products["product_id"].duplicated().sum())

sellers = pd.read_csv("data/raw/olist_sellers_dataset.csv")

print(sellers.shape)
print(sellers.isnull().sum())
print(sellers["seller_id"].duplicated().sum())

geolocation = pd.read_csv("data/raw/olist_geolocation_dataset.csv")
translation = pd.read_csv(
    "data/raw/product_category_name_translation.csv"
)

print("Geolocation shape:")
print(geolocation.shape)

print("Geolocation missing values:")
print(geolocation.isnull().sum())

print("Translation shape:")
print(translation.shape)

print("Translation missing values:")
print(translation.isnull().sum())