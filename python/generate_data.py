import pandas as pd
import numpy as np
import random
import os

from faker import Faker
from datetime import timedelta

fake = Faker()

random.seed(42)
np.random.seed(42)

os.makedirs("../source_data", exist_ok=True)

customers = []

for customer_id in range(1,10001):

    customers.append({
        "customer_id": customer_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": random.choice(["Male","Female"]),
        "email": fake.email(),
        "city": fake.city(),
        "state": fake.state(),
        "country": "USA",
        "signup_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    })

customers_df = pd.DataFrame(customers)


customers_df.to_csv(
    "../source_data/customers.csv",
    index=False
)

categories = {
    "Electronics":["Mobile","Laptop","Tablet"],
    "Fashion":["Shirt","Shoes","Jeans"],
    "Home":["Furniture","Kitchen","Decor"]
}

products = []

for product_id in range(1,2001):

    category = random.choice(
        list(categories.keys())
    )

    subcategory = random.choice(
        categories[category]
    )

    cost_price = round(
        random.uniform(10,500),2
    )

    selling_price = round(
        cost_price * random.uniform(1.2,2.0),2
    )

    products.append({
        "product_id": product_id,
        "product_name": f"{subcategory}_{product_id}",
        "category": category,
        "subcategory": subcategory,
        "brand": random.choice(
            ["Apple","Samsung","Dell","Nike","Sony"]
        ),
        "cost_price": cost_price,
        "selling_price": selling_price
    })

products_df = pd.DataFrame(products)


products_df.to_csv(
    "../source_data/products.csv",
    index=False
)

#Generate Stores

stores = []

for store_id in range(1,101):

    stores.append({
        "store_id": store_id,
        "store_name": f"Store_{store_id}",
        "city": fake.city(),
        "state": fake.state(),
        "country": "USA"
    })

stores_df = pd.DataFrame(stores)

stores_df.to_csv(
    "../source_data/stores.csv",
    index=False
)

####Generate Campaigns

campaigns = []

for campaign_id in range(1,51):

    start_date = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    campaigns.append({
        "campaign_id": campaign_id,
        "campaign_name": f"Campaign_{campaign_id}",
        "start_date": start_date,
        "end_date": start_date + timedelta(days=30),
        "budget": round(
            random.uniform(10000,100000),
            2
        )
    })

campaigns_df = pd.DataFrame(campaigns)

campaigns_df.to_csv(
    "../source_data/campaigns.csv",
    index=False
)

#Generate Orders

orders = []

for order_id in range(1,100001):

    orders.append({
        "order_id": order_id,
        "customer_id": random.randint(1,10000),
        "store_id": random.randint(1,100),
        "campaign_id": random.randint(1,50),
        "order_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
        "payment_type": random.choice(
            ["Cash","Card","UPI","Wallet"]
        )
    })

orders_df = pd.DataFrame(orders)


orders_df.to_csv(
    "../source_data/orders.csv",
    index=False
)

#Generate Order Items
order_items = []

for order_item_id in range(1,500001):

    quantity = random.randint(1,5)

    unit_price = round(
        random.uniform(20,500),
        2
    )

    order_items.append({
        "order_item_id": order_item_id,
        "order_id": random.randint(1,100000),
        "product_id": random.randint(1,2000),
        "quantity": quantity,
        "unit_price": unit_price,
        "sales_amount": round(
            quantity * unit_price,
            2
        )
    })

order_items_df = pd.DataFrame(order_items)

order_items_df.to_csv(
    "../source_data/order_items.csv",
    index=False
)


print(customers_df.shape)
print(products_df.shape)
print(stores_df.shape)
print(campaigns_df.shape)
print(orders_df.shape)
print(order_items_df.shape)