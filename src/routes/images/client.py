import os

from imagekitio import ImageKit

class ImageKitClient:
    def __init__(self):
        self.client = ImageKit(
            public_key=os.getenv("IMAGE_KIT_PUBLIC_KEY"),
            private_key=os.getenv("IMAGE_KIT_PRIVATE_KEY"),
            url_endpoint=os.getenv("IMAGE_KIT_ENDPOINT")
        )