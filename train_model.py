import pandas as pd
import mysql.connector
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib # To save the model
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Connect and Load
db = mysql.connector.connect(host="localhost", user="root", password="Ishan852006", database="supply_chain_db")
df = pd.read_sql("SELECT * FROM sales_leads", db)

# 2. FEATURE ENGINEERING (The most important part)
df['sale_date'] = pd.to_datetime(df['sale_date'])
df['day_of_week'] = df['sale_date'].dt.dayofweek
df['month'] = df['sale_date'].dt.month
# We don't need sale_date or sale_id for the math
X = df[['product_id', 'day_of_week', 'month', 'discount_applied']]
y = df['units_sold']

# 3. SPLIT: 80% to learn, 20% to test if it's lying
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. TRAIN: The Random Forest Regressor
# n_estimators=100 means we are using 100 decision trees to vote
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. EVALUATE: How many units are we off on average?
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

print(f"Model Trained. Mean Absolute Error: {mae:.2f} units")

# 6. SAVE: Save the brain to a file named 'demand_model.pkl'
joblib.dump(model, 'demand_model.pkl')
print("Model saved as demand_model.pkl")

import matplotlib.pyplot as plt
import seaborn as sns

# ... [Previous Training & Prediction Code] ...

# 1. EVALUATE
mae = mean_absolute_error(y_test, predictions)
print(f"Model Trained. Mean Absolute Error: {mae:.2f} units")

# 2. VISUALIZE (Add it here)
plt.figure(figsize=(12, 6))
plt.plot(y_test.values[:50], label='Actual Sales', color='#1f77b4', marker='o')
plt.plot(predictions[:50], label='Predicted Sales', color='#ff7f0e', linestyle='--', marker='x')
plt.title('Demand Forecasting Accuracy')
plt.legend()
plt.savefig('model_accuracy_plot.png')
print("Graph saved as model_accuracy_plot.png")

# 3. FEATURE IMPORTANCE (Add it here)
importances = model.feature_importances_
feature_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
print("\n--- Feature Importance ---")
print(feature_importance_df.sort_values(by='Importance', ascending=False))

# 4. SAVE THE BRAIN
joblib.dump(model, 'demand_model.pkl')
print("\nModel saved as demand_model.pkl")

# 5. CLOSE CONNECTION (Always Last)
db.close()
print("Database connection closed.")
plt.show() # This opens the window at the very end