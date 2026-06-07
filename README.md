# 🚨 Fraud Detection System (E-commerce + Credit Card)

## 📌 Overview
This project builds a fraud detection pipeline for:
- E-commerce transactions (with behavioral + geolocation data)
- Credit card transactions (anonymized PCA features)

The goal is to detect fraudulent activity while handling severe class imbalance using machine learning techniques.

---

## 📂 Project Structure
fraud-detection/
│
├── data/ (ignored in git)
├── models/ # Saved models & artifacts
├── notebooks/ # EDA, feature engineering, modeling
├── src/ # Reusable pipeline code
│ ├── data_loader.py
│ ├── preprocessing.py
├── scripts/ # Execution scripts
├── tests/ # Basic tests (future extension)
├── README.md

## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone <repo-url>
cd fraud-detection
2. Create environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
📊 Workflow
1. Data Loading
Fraud dataset
IP-to-country mapping
Credit card dataset
2. Preprocessing
Missing value handling
Duplicate removal
Data type conversion
3. Feature Engineering (E-commerce)
time_since_signup
hour_of_day
day_of_week
transaction_count
IP → Country mapping
4. Scaling & Encoding
StandardScaler for numerical features
OneHotEncoder for categorical features
5. Class Imbalance Handling
SMOTE applied ONLY on training data
🧠 Key Insights
Fraud is highly imbalanced (~9% or less)
Time-based behavior is a strong fraud indicator
Geolocation significantly improves fraud detection
Rapid transactions after signup are high-risk signals
📈 Modeling (Next Phase)
Logistic Regression (baseline)
Random Forest / XGBoost (ensemble)
Evaluation metrics:
F1 Score
AUC-PR
Confusion Matrix
🧩 Explainability (Next Phase)
SHAP analysis will be used to:
Explain model decisions
Identify key fraud drivers
Provide business recommendations
👨‍💻 Author

Fraud Detection Project — 10 Academy Week 5–6 Challenge


