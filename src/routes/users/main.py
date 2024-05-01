from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db_session
from src.routes.users.schemas import SaveUserRequest
from src.routes.users.services import UserService

router = APIRouter(
    prefix="/api/v1/users", 
    tags=["Users"],
    responses={ 404: { "description": "Not found" } }
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def save_user(request: SaveUserRequest, session: Session = Depends(get_db_session)):
    return UserService(session).save(request.to_model())