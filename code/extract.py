import requests

# Add your API key here
import requests
import json
import os

# Configuration
API_URL = "https://cent.ischool-iot.net/api/weather/forecast"
API_KEY = "89b6dc8fb35ed9372acafa46"  # Replace with your actual API key
OUTPUT_DIR = "data"
OUTPUT_FILE = "forecast_weather.json"

# Parameters for the API call
params = {
    "latitude": 43.04,     # Example: Syracuse, NY
    "longitude": -76.14,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "America/New_York"
}

headers = {
    "x-api-key": "89b6dc8fb35ed9372acafa46"
}

# Make sure the data folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Make the API request
response = requests.get(API_URL, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    # Save to file
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Forecast data saved to {output_path}")
else:
    print(f"❌ Error fetching data: {response.status_code} - {response.text}")
'''
def get_weather_for_month(year, month):
    url = "https://cent.ischool-iot.net/api/weather/forecast"
    start_date = f"{year}-{month:01d}-01"
    end_date = f"{year}-{month:12d}-28"  # Adjust the end date as needed
    params = {
        "start": start_date,
        "end": end_date,
        "lat": 43.0481,
        "lon": -76.1474
    }
    headers = {
        "x-api-key": "89b6dc8fb35ed9372acafa46"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        filename = f"historical_weather_{year}_{month:02d}.json"
        with open(filename, "w") as f:
            f.write(response.text)
        print(f"✅ Data saved to {filename}")
    else:
        print("❌ Error:", response.status_code)
        print(response.text)

if __name__ == "__main__":
    for year in range(2023, 2024):  # Adjust year range as needed
        for month in range(1, 13):
            get_weather_for_month(year, month)
'''