import pandas as pd
import mysql.connector

db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Ishan852006", # Replace with your Workbench password
        database="supply_chain_db",
        auth_plugin='mysql_native_password'
    )
cursor = db.cursor()

# Load data into Pandas
query = "SELECT * FROM sales_leads"
df = pd.read_sql(query, db)

# Convert sale_date to a real datetime object
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Create a 'is_weekend' column
df['is_weekend'] = df['sale_date'].dt.dayofweek >= 5

# Calculate the mean (average)
analysis = df.groupby('is_weekend')['units_sold'].mean()
print(analysis)