# Create this new file to bridge the gap between AI and Business
import joblib
import pandas as pd
import mysql.connector

model = joblib.load('demand_model.pkl')
db = mysql.connector.connect(host="localhost", user="root", password="Ishan852006", database="supply_chain_db")

# 1. Fetch current stock levels
inventory = pd.read_sql("SELECT * FROM inventory", db)

# 2. Predict demand for the next 3 days (The Lead Time)
# Logic: We check if current stock can survive the time it takes for a new order to arrive.
for index, row in inventory.iterrows():
    # Predicting for Product_ID, Day_of_Week, Month, Discount
    prediction = model.predict([[row['product_id'], 0, 2, 0.0]])[0] 
    
    # The 'Safety Stock' Logic
    if row['current_stock'] < (prediction * 1.5): # 1.5 is our safety buffer
        print(f"⚠️ ALERT: {row['name']} is CRITICAL. Forecast: {prediction:.1f} units. Current: {row['current_stock']}")
        print(f"ACTION: Order {int(prediction * 3)} units immediately.")
    else:
        print(f"✅ {row['name']} stock is healthy.")