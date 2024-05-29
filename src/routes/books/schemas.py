from sqlalchemy import or_, func
from pydantic import BaseModel, Field
from src.routes.authors.models import Author
from src.routes.books.models import *
from enum import Enum

class BookStatus(Enum):
    AVAILABLE = 'AVAILABLE'
    BORROWED = 'BORROWED'

class SaveBookRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=128)
    description: str | None = Field(None)
    comment: str | None = Field(None)
    pages: int | None = Field(None, ge=0)
    rating: int = Field(0, ge=0, le=5)
    status: BookStatus = Field(BookStatus.AVAILABLE)
    image_id: str | None = Field(None)
    author: str | None = Field(None, max_length=32)
    language: str | None = Field(None, max_length=32)
    publisher: str | None = Field(None, max_length=32)
    category: str | None = Field(None, max_length=32)
    subcategory: str | None = Field(None, max_length=32)

    def to_model(self):
        book = Book()
        book.name = self.name
        book.description = self.description
        book.comment = self.comment
        book.pages = self.pages
        book.rating = self.rating
        book.status = self.status.name
        book.image_id = self.image_id
        return book
    
class BookFilter(BaseModel):
    token: str | None = Field(None, max_length=128)
    rating: int | None = Field(None, ge=0, le=5)
    publisher_id: int | None = Field(None, ge=0)
    category_id: int | None = Field(None, ge=0)
    subcategory_id: int | None = Field(None, ge=0)

    def condition(self):
        conditions = []
        if self.token is not None:
            conditions.append(or_(func.lower(Book.name).contains(self.token.lower()), 
                                  func.lower(Book.description).contains(self.token.lower()),
                                  func.lower(Book.comment).contains(self.token.lower()),
                                  func.lower(Author.name).contains(self.token.lower())))
        if self.rating is not None:
            conditions.append(Book.rating == self.rating)
        if self.publisher_id is not None:
            conditions.append(Book.publisher_id == self.publisher_id)
        if self.category_id is not None:
            conditions.append(Book.category_id == self.category_id)
        if self.subcategory_id is not None:
            conditions.append(Book.subcategory_id == self.subcategory_id)
        return conditions