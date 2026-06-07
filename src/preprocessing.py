import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE


def merge_ip_data(fraud_df, ip_df):
    """
    Merge fraud dataset with IP-to-country mapping using range-based lookup.
    Includes basic validation and safety checks.
    """
    if fraud_df is None or ip_df is None:
        raise ValueError("Input dataframes cannot be None")

    fraud_df = fraud_df.sort_values('ip_address')
    ip_df = ip_df.sort_values('lower_bound_ip_address')

    merged_df = pd.merge_asof(
        fraud_df,
        ip_df,
        left_on='ip_address',
        right_on='lower_bound_ip_address',
        direction='backward'
    )

    merged_df = merged_df[
        merged_df['ip_address'] <= merged_df['upper_bound_ip_address']
    ]

    return merged_df


def create_features(df):
    """
    Create behavioral fraud detection features.
    Ensures datetime conversion for safety.
    """

    if df is None or df.empty:
        raise ValueError("Input dataframe is empty or None")

    df = df.copy()

    # ✅ FIX: ensure datetime conversion (VERY IMPORTANT)
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])

    df['time_since_signup'] = (
        df['purchase_time'] - df['signup_time']
    ).dt.total_seconds()

    df['hour_of_day'] = df['purchase_time'].dt.hour
    df['day_of_week'] = df['purchase_time'].dt.dayofweek

    freq = df['user_id'].value_counts()
    df['transaction_count'] = df['user_id'].map(freq)

    return df

def preprocess_and_balance(X_train, X_test, y_train):
    """
    Scale, encode, and apply SMOTE only on training data.
    """

    if X_train is None or X_test is None:
        raise ValueError("Train or test data is None")

    numeric_features = X_train.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X_train.select_dtypes(include=['object']).columns

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ]
    )

    # Fit ONLY on training data (prevents leakage)
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(
        X_train_processed, y_train
    )

    return X_train_resampled, X_test_processed, y_train_resampled, preprocessor