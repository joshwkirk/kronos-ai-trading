# training.py
import pandas as pd
def train_model(df):
    print("Training model on dataframe with", len(df), "rows")

def engineer_features(df):
    df["feature"] = df["close"].rolling(5).mean()
    return df
