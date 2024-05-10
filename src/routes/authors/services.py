from sqlalchemy.orm import Session
from src.routes.commons.base_service import BaseService
from src.routes.authors.models import Author

class AuthorService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Author)