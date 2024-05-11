from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.routes.commons.base_service import BaseService
from src.routes.books.models import Book

class BookService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Book)

    def save(self, book: Book):
        return super().save(book)

    def find_all(self, page: Page):
        return super().find_all(page)
    
    def delete_by_id(self, id: int):
        return super().delete_by_id(id)