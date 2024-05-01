from sqlalchemy.orm import Session
from src.routes.commons.base_service import BaseService
from src.routes.users.models import User

class UserService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, User)