import pandas as pd
import json
import os

# Set up cache folder path for saving data
CACHE_PATH = os.path.join("cache", "C:\Users\batis\IST 356 Program Tech\VS Code\project-kebatist\cache\raw_data.json")
DATA_PATH = os.path.join("data", "C:\Users\batis\IST 356 Program Tech\VS Code\project-kebatist\data\IMDB Top 250 Movies.csv")  # Replace with your actual file path

def load_and_process_data():
    # Load the CSV file into a pandas DataFrame
    try:
        df = pd.read_csv(DATA_PATH)
        print(f"✅ Loaded {len(df)} records from {DATA_PATH}")
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return []

    # Select relevant columns for simplicity (you can adjust these as needed)
    df_processed = df[['rank', 'name', 'year', 'rating', 'genre', 'certificate', 'run_time', 'tagline', 'budget', 'box_office', 'casts', 'directors', 'writers']]

    # Convert DataFrame to a list of dictionaries
    data = df_processed.to_dict(orient="records")

    return data

def save_to_cache(data, path=CACHE_PATH):
    # Save the processed data to JSON
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"✅ Saved {len(data)} items to {CACHE_PATH}")
    except Exception as e:
        print(f"Error saving data to cache: {e}")

if __name__ == "__main__":
    # Load and process the dataset
    data = load_and_process_data()

    # Save the processed data to cache
    if data:
        save_to_cache(data)

