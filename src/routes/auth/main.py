from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.config.database import get_db_session
from src.routes.auth.schemas import LoginRequest
from src.routes.auth.service import AuthService
from src.routes.commons.jwt_service import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        return jwt.get_user_email(token)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e.args[0])

@router.post("/")
def authenticate(request: LoginRequest, session: Session = Depends(get_db_session)):
    return AuthService(session).authenticate(request)

