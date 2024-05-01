from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.routes.auth.schemas import *
from src.routes.commons.jwt_service import jwt
from src.routes.users.services import UserService
from src.util.hash_password import are_equals_passwords

class AuthService:
    def __init__(self, session: Session):
        self.user_service = UserService(session)

    def authenticate(self, request: LoginRequest):
        try:
            user = self.user_service.find_by_email(request.email)
            if(not are_equals_passwords(request.password, user.password)):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
            return LoginResponse(token=jwt.generate_token(user.email))
        except HTTPException:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

