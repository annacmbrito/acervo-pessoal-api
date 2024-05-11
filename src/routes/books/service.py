from sqlalchemy.orm import Session
from src.routes.commons.base_service import BaseService
from src.routes.books.models import Book

class BookService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Book)

    def save(self, book: Book):
        return super().save(book)