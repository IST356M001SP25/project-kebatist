import streamlit as st
import pandas as pd
import json
import os
import streamlit as st
import pandas as pd
import json
import os

# Function to load multiple JSON files from the 'data' folder and cache the result
@st.cache_data
def load_multiple_files(file_pattern="historical_weather_*.json"):
    all_data = []
    # Specify the path to the 'data' folder
    data_folder = "data"
    files = [f for f in os.listdir(data_folder) if f.startswith("historical_weather") and f.endswith(".json")]
    
    if not files:
        st.error("❌ No weather data files found in the 'data' folder. Please run extract.py to fetch the data.")
        return None
    
    # Load each JSON file from the 'data' folder
    for file in files:
        file_path = os.path.join(data_folder, file)
        with open(file_path, "r") as f:
            data = json.load(f)
            all_data.append(data["daily"])  # Assuming "daily" contains the actual weather data
    
    return all_data

# Function to process data into DataFrame and cache the result
# Function to process data into DataFrame and cache the result
@st.cache_data
def process_data(data):
    try:
        # Combine all data from different files into a single DataFrame
        df = pd.concat([pd.DataFrame(d) for d in data], ignore_index=True)
        df["time"] = pd.to_datetime(df["time"])  # Convert time column to datetime format
        return df
    except Exception as e:
        st.error(f"Error processing data: {e}")
        return None

# Streamlit UI
st.title("📊 Historical Weather Dashboard")

# Load data from multiple files
data = load_multiple_files()

if data:
    # Process the loaded data into a DataFrame
    df = process_data(data)
    
    if df is not None:
        st.write("### Raw Data", df.head())
        st.line_chart(df.set_index("time")[["snowfall_sum"]])  # Change column name based on your data
