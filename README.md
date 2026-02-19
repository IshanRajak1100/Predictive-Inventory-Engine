Project Overview
This project addresses a core retail challenge: Optimizing stock levels through predictive analytics. By leveraging historical sales patterns, this system transitions inventory management from reactive "guessing" to proactive, data-driven decision-making.

Key Features
Predictive Demand Engine: Utilizes a Random Forest Regressor to forecast daily sales velocity with quantified accuracy.

Automated Replenishment Logic: A decision-support layer that calculates safety stock and triggers real-time restock alerts.

Feature Engineering: Extracts temporal intelligence (Day of week, seasonality) to capture non-linear consumer behaviors.

End-to-End Pipeline: Integrates a relational database (MySQL) with advanced analytics (Pandas) and Machine Learning (Scikit-Learn).

Technical Architecture
1. Data Engineering (The Foundation)
Schema Design: Implemented a normalized MySQL database to manage product metadata and high-frequency transaction logs.

Data Simulation: Engineered a custom Python simulation to generate historical datasets, incorporating realistic noise and specific "weekend-spike" biases for model validation.

2. Machine Learning & Analysis (The Brain)
EDA: Conducted statistical analysis using Pandas to validate correlation between temporal features and sales volume.

Modeling: Trained an ensemble model to handle multi-variable inputs (Product ID, Date, Discount status).

Evaluation: Monitored performance using Mean Absolute Error (MAE) to ensure forecast reliability.

Tech Stack
Language: Python

Database: MySQL

Libraries: Scikit-Learn, Pandas, NumPy, Matplotlib, Joblib

How to Use
Initialize Database: Run the provided SQL script in MySQL Workbench to set up the environment.

Generate History: Execute generate_data.py to populate the database with transactional history.

Train & Visualize: Run train_model.py. This generates the trained model (.pkl) and the accuracy visualization.

Execute Advisor: Run inventory_advisor.py to receive automated stock recommendations based on the latest predictions.
