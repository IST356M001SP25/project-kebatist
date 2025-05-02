import json

with open("historical_weather.json") as f:
    data = json.load(f)

print(data.keys())  # shows top-level keys
