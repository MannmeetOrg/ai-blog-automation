import requests

class SerpAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_trending_articles(self, keyword):
        url = f"https://serpapi.com/search?q={keyword}&api_key={self.api_key}"
        response = requests.get(url)
        return response.json()
