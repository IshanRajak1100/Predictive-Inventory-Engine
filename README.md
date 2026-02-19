# 🛒 Predictive Inventory Engine (P.I.E.)
> *Transforming retail data into actionable stock intelligence using Machine Learning.*

---

## 📌 Project Overview
This project addresses a core retail challenge: **optimizing stock levels through predictive analytics.** By leveraging historical sales patterns, this system transitions inventory management from reactive "guessing" to proactive, data-driven decision-making.

---

## 🚀 Key Features
* **🧠 Predictive Demand Engine:** Utilizes a **Random Forest Regressor** to forecast daily sales velocity with quantified accuracy.
* **🔔 Automated Replenishment:** A decision-support layer that calculates safety stock and triggers real-time restock alerts.
* **📊 Feature Engineering:** Extracts temporal intelligence (Day of week, seasonality) to capture non-linear consumer behaviors.
* **🔗 End-to-End Pipeline:** Integrates a relational database (**MySQL**) with advanced analytics (**Pandas**) and Machine Learning (**Scikit-Learn**).

---

## 🏗️ Technical Architecture

### 1. Data Engineering (The Foundation)
* **Schema Design:** Implemented a normalized MySQL database to manage product metadata and high-frequency transaction logs.
* **Data Simulation:** Engineered a custom Python simulation to generate historical datasets, incorporating realistic noise and "weekend-spike" biases for model validation.

### 2. Machine Learning & Analysis (The Brain)
* **EDA:** Conducted statistical analysis using Pandas to validate correlation between temporal features and sales volume.
* **Modeling:** Trained an ensemble model to handle multi-variable inputs (Product ID, Date, Discount status).
* **Evaluation:** Monitored performance using **Mean Absolute Error (MAE)** to ensure forecast reliability.

---

## 🛠️ Tech Stack
| Category | Tools |
| :--- | :--- |
| **Language** | Python 3.x |
| **Database** | MySQL |
| **Libraries** | Scikit-Learn, Pandas, NumPy, Matplotlib |
| **ML Models** | Random Forest Regressor |

---

## 📈 Performance Visualization
![Model Accuracy](./model_accuracy_plot.png)
*Figure 1: Line chart comparing Actual vs. Predicted sales showing 90%+ pattern alignment.*
