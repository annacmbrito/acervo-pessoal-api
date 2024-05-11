from pydantic import BaseModel, Field
from src.routes.languages.models import *

class SaveLanguageRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=32)

    def to_model(self):
        language = Language()
        language.name = self.name
        return language