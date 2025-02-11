# News Fetcher using NewsAPI

This Python script fetches the latest news headlines related to a specific topic using the [NewsAPI](https://newsapi.org/).

## Features
- Fetches top 5 news articles based on a given keyword.
- Displays the news title, source, and URL.
- Uses the `requests` module to interact with the NewsAPI.

## Prerequisites
- Python 3.x installed on your system.
- An API key from [NewsAPI](https://newsapi.org/).
- `requests` module installed.

## Installation
1. Clone this repository or copy the script.
2. Install required dependencies:
   ```bash
   pip install requests
   ```

## Usage
1. Replace `API_KEY` with your actual NewsAPI key in the script.
2. Run the script:
   ```bash
   python news_fetcher.py
   ```
3. By default, it fetches news related to "AI". You can modify the `get_news("your_topic")` function call to fetch news on other topics.

## Code Example
```python
import requests

# Replace with your actual NewsAPI key
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://newsapi.org/v2/top-headlines"

def get_news(q="AI"):
    params = {
        "apiKey": API_KEY,
        "q": q,
        "pageSize": 5
    }
    response = requests.get(BASE_URL, params=params)
    news_data = response.json()
    if news_data["status"] == "ok":
        articles = news_data["articles"]
        if articles:
            for idx, article in enumerate(articles, start=1):
                print(f"{idx}. {article['title']}")
                print(f"   Source: {article['source']['name']}")
                print(f"   URL: {article['url']}\n")
        else:
            print("No articles found.")
    else:
        print("Error fetching news:", news_data.get("message"))

if __name__ == "__main__":
    get_news("AI")
```

## API Limitations
- The free plan allows **100 requests per day**.
- The `top-headlines` endpoint may not return results for every topic.

## Future Enhancements
- Allow users to input a keyword dynamically.
- Add support for country-based filtering.
- Integrate a GUI or web interface.

## License
This project is open-source and available under the **MIT License**.

