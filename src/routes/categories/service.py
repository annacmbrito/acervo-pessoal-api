from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.routes.commons.base_service import BaseService
from src.routes.categories.models import Category

class CategoryService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Category)

    def find_all(self, page: Page):
        return super().find_all(page)

    def save(self, category: Category):
        return super().save(category)
    
    def delete_by_id(self, id: int):
        return super().delete_by_id(id)