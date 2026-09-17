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