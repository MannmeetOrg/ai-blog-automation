class ResearchAgent:
    def __init__(self, serpapi_client):
        self.serpapi = serpapi_client

    def fetch_trends(self, keyword):
        return self.serpapi.get_trending_articles(keyword)
