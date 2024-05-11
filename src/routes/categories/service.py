from sqlalchemy.orm import Session
from src.routes.commons.base_service import BaseService
from src.routes.categories.models import Category

class CategoryService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Category)