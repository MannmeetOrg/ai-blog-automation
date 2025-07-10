class WriterAgent:
    def __init__(self, ai_client):
        self.ai = ai_client

    def generate_article(self, prompt):
        return self.ai.complete(prompt)
