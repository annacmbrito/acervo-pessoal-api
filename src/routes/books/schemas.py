from pydantic import BaseModel, Field
from src.routes.books.models import *
from enum import Enum

class BookStatus(Enum):
    AVAILABLE = 'AVAILABLE'
    BORROWED = 'BORROWED'

class SaveBookRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=128)
    description: str = Field('')
    comment: str = Field('')
    pages: int = Field(0, ge=0)
    rating: int = Field(0, ge=0, le=5)
    status: BookStatus = Field(BookStatus.AVAILABLE)
    author: str = Field(..., min_length=3, max_length=32)
    language: str = Field(..., min_length=3, max_length=32)
    publisher: str = Field(..., min_length=3, max_length=32)
    category: str = Field(..., min_length=3, max_length=32)
    subcategory: str = Field(..., min_length=3, max_length=32)

    def to_model(self):
        book = Book()
        book.name = self.name
        book.description = self.description
        book.comment = self.comment
        book.pages = self.pages
        book.rating = self.rating
        book.status = self.status.name
        return book