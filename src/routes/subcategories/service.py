from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.routes.commons.base_service import BaseService
from src.routes.subcategories.models import Subcategory

class SubcategoryService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Subcategory)

    def find_all(self, page: Page):
        return super().find_all(page)

    def save(self, book: Subcategory):
        return super().save(book)