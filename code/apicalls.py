import requests

# Add your API key here
API_KEY = "89b6dc8fb35ed9372acafa46"

def get_weather():
    location = "New York"
    start_date = "2023-09-21"
    end_date = "2023-09-28"

    url = f"https://cent.ischool-iot.net/api/weather/historical"
    params = {
        "unitGroup": "metric",
        "include": "days",
        "key": API_KEY,
        "contentType": "json"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        with open("historical_weather.json", "w") as f:
            f.write(response.text)
        print("✅ Weather data saved to historical_weather.json")
    else:
        print("❌ Error:", response.status_code)


'''
def get_azure_sentiment(text: str) -> dict:
    """
    Given a text input, return the sentiment analysis results from Azure API.
    """
    header = { 'X-API-KEY': APIKEY }  # Use the APIKEY variable for consistency
    data = { 'text': text }
    url = "https://new-api-path.net/api/azure/sentiment"  # Updated API path

    response = requests.post(url=url, headers=header, data=data)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()  # Return the JSON response as a dictionary
'''

def get_azure_key_phrase_extraction(text: str) -> dict:
    header = { 'X-API-KEY': "89b6dc8fb35ed9372acafa46" }
    data = { 'text': text }
    url = "https://cent.ischool-iot.net/api/azure/keyphrasextraction"
    response = requests.post(url=url, headers=header, data=data)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary
    #pass # Implement this function

def get_azure_named_entity_recognition(text: str) -> dict:
    header = { 'X-API-KEY': "89b6dc8fb35ed9372acafa46" }
    data = { 'text': text }
    url = "https://cent.ischool-iot.net/api/azure/entityrecognition"
    response = requests.post(url=url, headers=header, data=data)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary
    pass # Implement this function


def geocode(place:str) -> dict:
    '''
    Given a place name, return the latitude and longitude of the place.
    Written for example_etl.py
    '''
    header = { 'X-API-KEY': "89b6dc8fb35ed9372acafa46" }
    params = { 'location': place }
    url = "https://cent.ischool-iot.net/api/google/geocode"
    response = requests.get(url=url, headers=header, params=params)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary


def get_weather(lat: float, lon: float) -> dict:
    '''
    Given a latitude and longitude, return the current weather at that location.
    written for example_etl.py
    '''
    header = { 'X-API-KEY': "89b6dc8fb35ed9372acafa46" }
    params = { 'lat': lat, 'lon': lon, 'units': 'imperial' }
    url = "https://cent.ischool-iot.net/api/weather/current"
    response = requests.get(url, headers=header, params=params)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary

if __name__ == '__main__':
    # Test the functions here if needed
    # Example: print(get_google_place_details('ChIJN1t_tDeuEmsRUsoyG83frY4'))
    pass  # Implement this function to test the API calls
    # Example: print(get_azure_sentiment('I love programming!'))
'''
# 👇 Replace this with your actual API key
API_KEY = "your_api_key_here"

def get_air_quality(lat, lon):
    """Fetch air quality data from OpenWeather API."""
    url = f"http://api.openweathermap.org/data/2.5/air_pollution"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get data. Status code:", response.status_code)
        print("Response:", response.text)
        return None

def save_data(data):
    """Save data to cache/raw_data.json"""
    os.makedirs("cache", exist_ok=True)
    with open("cache/raw_data.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Data saved to cache/raw_data.json")

if __name__ == "__main__":
    # Example: New York City
    lat = 40.73
    lon = -74.00

    data = get_air_quality(lat, lon)
    if data:
        save_data(data)
        print("Data fetched successfully.")
        '''
