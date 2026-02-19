import mysql.connector
import random
from datetime import datetime, timedelta

db = None
# 1. Establish the tunnel to MySQL
try:
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Ishan852006", # Replace with your Workbench password
        database="supply_chain_db",
        auth_plugin='mysql_native_password'
    )
    cursor = db.cursor()

    # 2. Seed the Inventory (The Products)
    # We use 'IGNORE' so it doesn't crash if you run the script twice
    products_sql = "INSERT IGNORE INTO inventory (name, current_stock, unit_cost, selling_price, reorder_point) VALUES (%s, %s, %s, %s, %s)"
    product_data = [
        ('Gaming Laptop', 50, 800.00, 1200.00, 10),
        ('Wireless Mouse', 200, 15.00, 45.00, 40),
        ('Mechanical Keyboard', 100, 40.00, 95.00, 20)
    ]
    cursor.executemany(products_sql, product_data)
    db.commit()

    # 3. Generate 100 days of Sales History
    sales_sql = "INSERT INTO sales_leads (product_id, sale_date, units_sold, discount_applied) VALUES (%s, %s, %s, %s)"
    
    start_date = datetime.now() - timedelta(days=100)
    
    for i in range(100):
        current_date = (start_date + timedelta(days=i)).date()
        is_weekend = current_date.weekday() >= 5 # 5 is Saturday, 6 is Sunday
        
        for p_id in range(1, 4): # For our 3 products
            # LOGIC: If it's a weekend, sales are 2x to 4x higher
            if is_weekend:
                sales = random.randint(10, 20)
            else:
                sales = random.randint(2, 8)
                
            discount = random.choice([0.0, 0.0, 0.1, 0.2]) # 25% chance of a discount
            
            cursor.execute(sales_sql, (p_id, current_date, sales, discount))
    
    db.commit()
    print(f"Successfully inserted {cursor.rowcount * 100} rows into sales_leads!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if db.is_connected():
        cursor.close()
        db.close()