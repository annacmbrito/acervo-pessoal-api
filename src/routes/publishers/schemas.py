from pydantic import BaseModel, Field
from src.routes.publishers.models import *

class SavePublisherRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=32)

    def to_model(self):
        publisher = Publisher()
        publisher.name = self.name
        return publisher