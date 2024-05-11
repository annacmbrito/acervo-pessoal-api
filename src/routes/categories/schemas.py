from pydantic import BaseModel, Field
from src.routes.categories.models import *

class SaveCategoryRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=32)

    def to_model(self):
        category = Category()
        category.name = self.name
        return category