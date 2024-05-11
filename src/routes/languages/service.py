from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.routes.commons.base_service import BaseService
from src.routes.languages.models import Language

class LanguageService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Language)

    def find_all(self, page: Page):
        return super().find_all(page)

    def save(self, language: Language):
        return super().save(language)
    
    def delete_by_id(self, id: int):
        return super().delete_by_id(id)