from pydantic import BaseModel, Field
from src.routes.subcategories.models import *

class SaveSubcategoryRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=32)
    category_id: int = Field(..., ge=1, alias="categoryId")

    def to_model(self):
        subcategory = Subcategory()
        subcategory.name = self.name
        subcategory.category_id = self.category_id
        return subcategory