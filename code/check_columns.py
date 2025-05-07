import pandas as pd
import os

csv_path = csv_path = "C:/Users/batis/IST 356 Program Tech/VS Code/project-kebatist/data/IMDB Top 250 Movies.csv"

df = pd.read_csv(csv_path)
print("Columns:", df.columns.tolist())