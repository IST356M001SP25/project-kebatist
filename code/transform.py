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
import pandas as pd

def transform_data(csv_path):
    # Load the CSV into a pandas DataFrame
    df = pd.read_csv(csv_path)

    # Print out the column names to inspect them
    print("Columns in the dataset:", df.columns)

    # Standardize column names to lowercase for consistency (optional)
    df.columns = df.columns.str.strip().str.lower()

    # Select the relevant columns (case-insensitive now)
    df_transformed = df[['rank', 'name', 'year', 'rating', 'genre', 'certificate', 'run_time', 'tagline', 'budget', 'box_office', 'casts', 'directors', 'writers']]

    # Convert 'Year' to integer, 'Rating' to float, and 'Votes' to integer
    df_transformed['year'] = pd.to_numeric(df_transformed['year'], errors='coerce')
    df_transformed['rating'] = pd.to_numeric(df_transformed['rating'], errors='coerce')
    df_transformed['rank'] = pd.to_numeric(df_transformed['rank'], errors='coerce')

    # Return the transformed DataFrame
    return df_transformed

# Test the function
if __name__ == "__main__":
    csv_path = r"C:\Users\batis\IST 356 Program Tech\VS Code\project-kebatist\data\IMDB Top 250 Movies.csv"
    transformed_data = transform_data(csv_path)

    # Display the first few rows of the transformed data
    print(transformed_data.head())

    # code/transform.py
