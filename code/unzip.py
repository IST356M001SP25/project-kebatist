import zipfile
import os

zip_path = "imdb-top-250-movies-dataset.zip"
extract_to = "data"

# Create data folder if it doesn't exist
os.makedirs(extract_to, exist_ok=True)

# Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("✅ Dataset extracted to 'data/'")
