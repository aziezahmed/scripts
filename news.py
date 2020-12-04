import requests
import json
import os
from unidecode import unidecode

def main():
    api_key = os.environ.get("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={api_key}"

    response = requests.get(url)
    data = response.json()
    if data["status"] != "error":
        articles = data["articles"]
        for article in articles:
            print(article["title"])
            if article["description"] is not None:
                print(unidecode(article["description"]))
                print("")

if __name__ == "__main__":
    main()
