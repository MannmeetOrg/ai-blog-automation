import requests

class DevtoClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def publish_article(self, title, body, tags):
        url = "https://dev.to/api/articles"
        headers = {"api-key": self.api_key}
        payload = {
            "article": {
                "title": title,
                "published": True,
                "body_markdown": body,
                "tags": tags
            }
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
