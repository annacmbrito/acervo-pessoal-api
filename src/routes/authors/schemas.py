from pydantic import BaseModel, Field
from src.routes.authors.models import *

class SaveAuthorRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=32)

    def to_model(self):
        author = Author()
        author.name = self.name
        return author