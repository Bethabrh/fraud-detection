# Fraud Detection Project (Task 1 - Interim Submission)

## Overview
This project focuses on detecting fraudulent transactions in two domains:

1. E-commerce transactions  
2. Credit card transactions  

The objective is to analyze transaction behavior, engineer meaningful features, and prepare high-quality datasets for machine learning-based fraud detection.

Fraud detection is a high-impact problem where both false positives and false negatives carry significant financial and operational costs.

---

## Datasets Used

- **Fraud_Data.csv** → E-commerce transaction data  
- **creditcard.csv** → Bank credit card transactions (PCA-transformed features)  
- **IpAddress_to_Country.csv** → IP geolocation mapping for country-level enrichment  

---

## Work Completed (Task 1)

### 1. E-commerce Fraud Dataset

- Data cleaning and validation
- Exploratory Data Analysis (EDA)
- Fraud class distribution analysis
- IP address → country mapping (geolocation enrichment)

#### Feature Engineering:
- time_since_signup → detects rapid fraudulent activity
- hour_of_day → captures unusual transaction timing
- day_of_week → captures weekly behavioral patterns
- transaction_count → detects abnormal user frequency patterns

- Country-level fraud rate analysis

---

### 2. Credit Card Dataset

- Exploratory Data Analysis (EDA)
- Class imbalance analysis
- Transaction amount distribution analysis
- Correlation analysis of PCA features

---

## Key Insights

- Both datasets are highly imbalanced, requiring specialized evaluation metrics (F1-score, AUC-PR)
- Fraudulent behavior shows strong temporal and behavioral patterns
- Geolocation (country) is a strong indicator of fraud risk
- User behavior features significantly improve fraud detection capability
- Traditional accuracy is not a suitable evaluation metric for this problem

---

## Next Steps (Task 2 & 3)

- Apply resampling techniques (SMOTE / undersampling)
- Train baseline and ensemble models (Logistic Regression, Random Forest, XGBoost)
- Evaluate using F1-score, confusion matrix, and AUC-PR
- Model explainability using SHAP for feature interpretation

---

## Status
Task 1 completed successfully. Dataset is fully prepared for model development in Task 2.