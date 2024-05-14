from sqlalchemy.orm import Session
from src.routes.commons.base_service import BaseService
from src.routes.publishers.models import Publisher

class PublisherService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Publisher)