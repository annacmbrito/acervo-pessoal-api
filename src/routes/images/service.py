from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.routes.commons.base_service import BaseService
from src.routes.images.models import Image

class ImageService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Image)

    def find_all(self, page: Page):
        return super().find_all(page)

    def save(self, image: Image):
        return super().save(image)