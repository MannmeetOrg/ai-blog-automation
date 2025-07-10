class BlogWorkflow:
    def __init__(self, research_agent, writer_agent, image_agent, qa_agent, devto_client):
        self.research = research_agent
        self.writer = writer_agent
        self.image = image_agent
        self.qa = qa_agent
        self.devto = devto_client

    def run(self, topic, audience, tone):
        trends = self.research.fetch_trends(topic)
        prompt = f"Write a blog on {topic} for {audience} in a {tone} tone. Include: {trends}"
        article = self.writer.generate_article(prompt)
        image_url = self.image.generate_image(topic)
        checks = self.qa.run_checks(article)
        if checks["plagiarism"]["score"] < 0.1 and checks["seo"]["score"] > 80:
            self.devto.publish_article(f"{topic} - {tone}", article, ["ai", "automation"])
        return {"article": article, "checks": checks, "image": image_url}
