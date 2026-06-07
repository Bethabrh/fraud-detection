import pandas as pd

def load_data(fraud_path: str, ip_path: str):
    """
    Load fraud dataset and IP-to-country mapping dataset.
    """
    fraud_df = pd.read_csv(fraud_path)
    ip_df = pd.read_csv(ip_path)
    
    return fraud_df, ip_df
