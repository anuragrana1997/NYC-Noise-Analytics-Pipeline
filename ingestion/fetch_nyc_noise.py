import requests
from pathlib import Path
from datetime import datetime, timezone
import json

API_URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"

params = {
    "$where": "complaint_type like 'Noise%'",
    "$limit": 1000,
    "$order": "created_date DESC"
}

response = requests.get(API_URL, params=params, timeout=30)
response.raise_for_status()

records = response.json()

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
output_file = output_dir / f"nyc_noise_{timestamp}.jsonl"

with output_file.open("w", encoding="utf-8") as f:
    for record in records:
        f.write(json.dumps(record) + "\n")

print(f"Downloaded {len(records)}")
print(f"Saved to {output_file}")