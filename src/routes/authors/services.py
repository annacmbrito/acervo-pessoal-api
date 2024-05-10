from sqlalchemy.orm import Session
from src.routes.commons.base_service import BaseService
from src.routes.authors.models import Author

class AuthorService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Author)

    def find_all(self):
        return super().find_all()
    
    def save(self, author: Author):
        return super().save(author)
