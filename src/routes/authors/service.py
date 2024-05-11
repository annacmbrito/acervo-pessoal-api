from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.routes.commons.base_service import BaseService
from src.routes.authors.models import Author

class AuthorService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Author)

    def find_all(self, page: Page):
        return super().find_all(page)
    
    def save(self, author: Author):
        return super().save(author)
    
    def delete_by_id(self, id: int):
        return super().delete_by_id(id)
