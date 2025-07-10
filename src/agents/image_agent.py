class ImageAgent:
    def __init__(self, image_api_client):
        self.image_api = image_api_client

    def generate_image(self, description):
        return self.image_api.create_image(description)
