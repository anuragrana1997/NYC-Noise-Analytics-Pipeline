import requests
import json

API_URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"

params = {
    "$where": "complaint_type like 'Noise%'",
    "$limit": 100,
    "$order": "created_date DESC"
}

response = requests.get(API_URL, params=params, timeout=30)
response.raise_for_status()

records = response.json()

print(f"Number of records: {len(records)}")

if records:
    print(json.dumps(records[0], indent=2))