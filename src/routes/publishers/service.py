from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.routes.commons.base_service import BaseService
from src.routes.publishers.models import Publisher

class PublisherService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Publisher)

    def find_all(self, page: Page):
        return super().find_all(page)

    def save(self, publisher: Publisher):
        return super().save(publisher)
    
    def delete_by_id(self, id: int):
        return super().delete_by_id(id)