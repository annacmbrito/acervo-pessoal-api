from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.routes.commons.base_service import BaseService
from src.routes.users.models import User

class UserService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, User)

    def save(self, user: User):
        if(super().exists(User.email == user.email)):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")
        return super().save(user)