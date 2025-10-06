import pandas as pd
import os

def transform_data(df):
    df["fetched_at"] = pd.to_datetime(df["fetched_at"])
    df = df.sort_values("fetched_at")

    df["bitcoin.change_pct"] = df["bitcoin.usd"].pct_change() * 100
    df["ethereum.change_pct"] = df["ethereum.usd"].pct_change() * 100

    return df

def save_processed_data(df, processed_dir="data/processed"):
    os.makedirs(processed_dir, exist_ok=True)
    output_path = os.path.join(processed_dir, "crypto_prices_processed.csv")
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to: {output_path}")