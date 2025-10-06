import os
import json
import pandas as pd

def load_raw_data(raw_dir = "data/raw"):
    records = []

    for filename in os.listdir(raw_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(raw_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                records.append(data)

    df = pd.json_normalize(records)
    return df

