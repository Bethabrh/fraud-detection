# Fraud Detection Project (Task 1 - Interim Submission)

## Overview
This project focuses on detecting fraudulent transactions in two domains:
1. E-commerce transactions
2. Credit card transactions

The goal is to analyze patterns, engineer meaningful features, and prepare the data for machine learning models.

---

## Datasets Used
- Fraud_Data.csv → E-commerce transaction data
- creditcard.csv → Bank credit card transactions
- IpAddress_to_Country.csv → IP geolocation mapping

---

## Work Completed (Task 1)

### E-commerce Fraud Dataset
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Fraud distribution analysis
- Feature engineering:
  - time_since_signup
  - hour_of_day
  - day_of_week
  - transaction_count
- IP address to country mapping
- Country-level fraud analysis

### Credit Card Dataset
- Exploratory Data Analysis
- Class imbalance analysis
- Feature distribution analysis
- Correlation analysis

---

## Key Insights
- Both datasets are highly imbalanced
- Fraud behavior varies across geography and time
- User behavior features are strong fraud indicators
- Class imbalance requires specialized handling (SMOTE planned for modeling stage)

---

## Status
Task 1 completed. Ready for model building in Task 2.