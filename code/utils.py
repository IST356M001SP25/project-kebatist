# code/utils.py

import os
import pandas as pd
import json

# Define cache paths
RAW_PATH = os.path.join("cache", "raw_data.json")
CLEAN_PATH = os.path.join("cache", "clean_data.csv")

def save_json(data, path=RAW_PATH):
    """Save data to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_json(path=RAW_PATH):
    """Load data from a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_clean_csv(df, path=CLEAN_PATH):
    """Save cleaned DataFrame to CSV."""
    df.to_csv(path, index=False)

def load_clean_csv(path=CLEAN_PATH):
    """Load cleaned CSV into DataFrame."""
    return pd.read_csv(path)
