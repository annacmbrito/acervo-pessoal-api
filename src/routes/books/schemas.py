from pydantic import BaseModel, Field
from src.routes.books.models import *

class SaveBookRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=32)
    description: str = Field(..., min_length=3)
    comment: str = Field(..., min_length=3)
    rating: int = Field(0, ge=0, le=5)
    available: bool = Field(False)
    author_id: int = Field(..., ge=0)
    language_id: int = Field(..., ge=0)
    category_id: int = Field(..., ge=0)
    subcategory_id: int = Field(..., ge=0)

    def to_model(self):
        book = Book()
        book.name = self.name
        book.description = self.description
        book.comment = self.comment
        book.rating = self.rating
        book.available = self.available
        book.author_id = self.author_id
        book.language_id = self.language_id
        book.category_id = self.category_id
        book.subcategory_id = self.subcategory_id
        return book