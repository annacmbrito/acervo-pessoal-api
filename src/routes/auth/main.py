from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.database import get_db_session
from src.routes.auth.schemas import LoginRequest
from src.routes.auth.services import AuthService

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)

@router.post("/")
def authenticate(request: LoginRequest, session: Session = Depends(get_db_session)):
    return AuthService(session).authenticate(request)