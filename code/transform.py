'''import pandas as pd

def transform_data(csv_path):
    # Load the CSV into a pandas DataFrame
    df = pd.read_csv(csv_path)

# Select the relevant columns
df_transformed = df[['rank', 'name', 'year', 'rating', 'genre', 'certificate', 'run_time', 'tagline', 'budget', 'box_office', 'casts', 'directors', 'writers']]

# Convert 'Year' to integer, 'Rating' to float, and 'Votes' to integer
df_transformed['year'] = pd.to_numeric(df_transformed['year'], errors='coerce')
df_transformed['rating'] = pd.to_numeric(df_transformed['rating'], errors='coerce')
df_transformed['rank'] = pd.to_numeric(df_transformed['rank'], errors='coerce')

# Drop rows with missing values in key columns
df_transformed.dropna(subset=['rank', 'year', 'rating', 'run_time'], inplace=True)

# Reset the index of the DataFrame
df_transformed.reset_index(drop=True, inplace=True)
# Test the function
if __name__ == "__main__":
    csv_path = "C:/Users/batis/IST 356 Program Tech/VS Code/project-kebatist/data/IMDB Top 250 Movies.csv"
    transformed_data = transform_data(csv_path)
    print(transformed_data.head())  # Display the first few rows of the transformed data
# yas this codeis good and fire girl
'''
import os
import json
import pandas as pd

RAW_PATH = os.path.join("cache", "raw_data.json")
CLEAN_PATH = os.path.join("cache", "clean_data.csv")

def transform_data():
    # Load raw data
    with open(RAW_PATH, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    # Convert to DataFrame
    df = pd.DataFrame(raw_data)

    # Optional: Clean/transform columns
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Convert data types if needed
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    # Save to CSV
    df.to_csv(CLEAN_PATH, index=False)
    print(f"Transformed data saved to {CLEAN_PATH}")

    return df

if __name__ == "__main__":
    df_clean = transform_data()
    print(df_clean.head())
