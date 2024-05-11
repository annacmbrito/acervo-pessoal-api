from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.routes.commons.base_service import BaseService
from src.routes.subcategories.models import Subcategory
from src.routes.subcategories.schemas import SubcategoryFilter

class SubcategoryService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Subcategory)

    def find_all(self, filter: SubcategoryFilter, page: Page):
        return super().find_all(page, filter.condition())

    def save(self, book: Subcategory):
        return super().save(book)
    
    def delete_by_id(self, id: int):
        return super().delete_by_id(id)