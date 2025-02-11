"""
Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application

"""
import requests

# Replace with your actual NewsAPI key
API_KEY = "cd52220d58f2490fb62f64dfc0435e9c"
BASE_URL = "https://newsapi.org/v2/top-headlines"

def get_news(q = "AI"):
    """Fetch top headlines based on category and country."""
    params = {
        "apiKey": API_KEY,
        "q": q,
        "pageSize": 5  # Fetch top 5 articles
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
    # topic = input("Enter news category (business, entertainment, health, science, sports, technology): ").strip().lower()
    get_news("AI")

