# 📊 Customer Retention & Churn Analysis Report

## 📌 Project Overview
This project analyzes customer churn behavior using the Telco Customer Churn dataset.  
The goal is to identify why customers leave and what factors influence retention.

The analysis is presented through an interactive Streamlit dashboard.

---

## 🎯 Objectives
- Understand customer churn patterns
- Identify high-risk customer segments
- Analyze impact of contract type, internet service, and payment method
- Calculate key business KPIs
- Provide actionable business recommendations

---

## 📂 Dataset Information
- Source: Telco Customer Churn Dataset
- Records: Customer subscription data
- Features include:
  - Gender
  - Contract type
  - Internet service
  - Payment method
  - Monthly charges
  - Tenure
  - Churn status

---

## 🧹 Data Cleaning Steps
- Removed duplicate records
- Converted TotalCharges to numeric
- Handled missing values
- Standardized column names

---

## 🧠 Feature Engineering
- Created **Customer Lifetime Value (CLV)**
- Created **Tenure Groups**
  - 0–1 Year
  - 1–2 Years
  - 2–4 Years
  - 4–5 Years
  - 5+ Years

---

## 📊 Key Performance Indicators (KPIs)
- Total Customers
- Churned Customers
- Retained Customers
- Churn Rate
- Retention Rate
- Average Monthly Charges
- Average Tenure
- Average CLV

---

## 📈 Key Insights
- Month-to-month customers have the highest churn rate
- Customers with high monthly charges are more likely to churn
- Early-stage customers (0–12 months) are at highest risk
- Electronic check payment users show higher churn
- Fiber optic internet users have higher churn compared to others

---

## 🚀 Recommendations
- Promote long-term contracts (annual/bi-annual plans)
- Improve onboarding experience for new customers
- Offer discounts for high monthly charge users
- Encourage automatic payment methods
- Focus retention strategies on first-year customers

---

## 🛠 Tools Used
- Python
- Pandas
- Streamlit
- Plotly Express

---

## 📌 Conclusion
This analysis helps identify key drivers of churn and provides actionable insights to improve customer retention and increase business revenue.

---