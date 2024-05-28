from sqlalchemy.orm import Session
from src.routes.commons.base_service import BaseService
from src.routes.images.models import Image

class ImageService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Image)