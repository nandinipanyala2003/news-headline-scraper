from scraper import scrape_headlines
from utils import save_to_json, save_to_csv
from config import URLS, KEYWORD

def main():
    all_data = []

    for url in URLS:
        print(f"Scraping: {url}")
        data = scrape_headlines(url)

        if KEYWORD:
            data = [d for d in data if KEYWORD.lower() in d['title'].lower()]

        all_data.extend(data)

    if all_data:
        save_to_json(all_data, "data/headlines.json")
        save_to_csv(all_data, "data/headlines.csv")
        print("✅ Data saved successfully!")
    else:
        print("⚠️ No data found")

if __name__ == "__main__":
    main()