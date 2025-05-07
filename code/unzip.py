import zipfile
import os

zip_path = "imdb-top-250-movies-dataset.zip"
extract_to = "data"

os.makedirs(extract_to, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("✅ Extracted to 'data/' folder")
print("✅ Extracted to 'data/' folder")