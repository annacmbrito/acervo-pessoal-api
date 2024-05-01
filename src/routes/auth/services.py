from sqlalchemy.orm import Session
from src.routes.users.services import UserService

class AuthService:
    def __init__(self, session: Session):
        self.user_service = UserService(session)

