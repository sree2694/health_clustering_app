from sklearn.preprocessing import StandardScaler
import pandas as pd

def preprocess_data(df):
    df = df.select_dtypes(include=["float64", "int64"])  # numerical only
    df = df.dropna()
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)
    return df, scaled
