import requests
from bs4 import BeautifulSoup
import time
from utils import get_headers, handle_error

def scrape_headlines(url):
    headlines = []

    try:
        response = requests.get(url, headers=get_headers(), timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Example: works for many news sites (adjust if needed)
        articles = soup.find_all("a")

        for article in articles:
            title = article.get_text(strip=True)
            link = article.get("href")

            if title and link and len(title) > 30:
                headlines.append({
                    "title": title,
                    "url": link,
                    "time": "N/A"
                })

        time.sleep(2)  # respect delay

    except Exception as e:
        handle_error(e)

    return headlines