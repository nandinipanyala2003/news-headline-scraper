import json
import csv
import random

def get_headers():
    return {
        "User-Agent": "Mozilla/5.0"
    }

def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def save_to_csv(data, filename):
    if not data:
        return

    keys = data[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def handle_error(error):
    print(f"❌ Error: {error}")
    with open("logs/scraper.log", "a") as f:
        f.write(str(error) + "\n")