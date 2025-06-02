import pandas as pd
import mysql.connector

# Load CSV data
df = pd.read_csv("C:/Users/purte/OneDrive - Syracuse University/Documents/Sem-2/IST722 - DWH - Joseph Kinn/DWH Project/data.csv")

# Replace NaN with None
df = df.where(pd.notnull(df), None)

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="************",  
    database="food_delivery_dw"
)
cursor = conn.cursor()

# Create staging_orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS staging_orders (
    Customer_placed_order_datetime VARCHAR(50),
    Placed_order_with_restaurant_datetime VARCHAR(50),
    Driver_at_restaurant_datetime VARCHAR(50),
    Delivered_to_consumer_datetime VARCHAR(50),
    Driver_ID INT,
    Restaurant_ID INT,
    Consumer_ID INT,
    Is_New BOOLEAN,
    Delivery_Region VARCHAR(100),
    Is_ASAP BOOLEAN,
    Order_total FLOAT,
    Amount_of_discount FLOAT,
    Amount_of_tip FLOAT,
    Refunded_amount FLOAT
)
""")

# Insert data row by row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO staging_orders (
            Customer_placed_order_datetime, Placed_order_with_restaurant_datetime,
            Driver_at_restaurant_datetime, Delivered_to_consumer_datetime,
            Driver_ID, Restaurant_ID, Consumer_ID,
            Is_New, Delivery_Region, Is_ASAP,
            Order_total, Amount_of_discount, Amount_of_tip, Refunded_amount
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row.get('Customer_placed_order_datetime'),
        row.get('Placed_order_with_restaurant_datetime'),
        row.get('Driver_at_restaurant_datetime'),
        row.get('Delivered_to_consumer_datetime'),
        int(row['Driver_ID']) if row['Driver_ID'] is not None else None,
        int(row['Restaurant_ID']) if row['Restaurant_ID'] is not None else None,
        int(row['Consumer_ID']) if row['Consumer_ID'] is not None else None,
        bool(row['Is_New']) if row['Is_New'] is not None else None,
        row.get('Delivery_Region'),
        bool(row['Is_ASAP']) if row['Is_ASAP'] is not None else None,
        float(row['Order_total']) if row['Order_total'] is not None else None,
        float(row['Amount_of_discount']) if row['Amount_of_discount'] is not None else None,
        float(row['Amount_of_tip']) if row['Amount_of_tip'] is not None else None,
        float(row['Refunded_amount']) if row['Refunded_amount'] is not None else None
    ))

# Commit and close
conn.commit()
cursor.close()
conn.close()

