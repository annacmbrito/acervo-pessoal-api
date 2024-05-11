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
    
class SubcategoryFilter(BaseModel):
    name: str | None = Field(None, max_length=32)
    category_id: int | None = Field(None, ge=1, alias="categoryId")

    def condition(self):
        conditions = []
        if self.name is not None:
            conditions.append(Subcategory.name.contains(self.name))
        if self.category_id is not None:
            conditions.append(Subcategory.category_id == self.category_id)
        return conditions