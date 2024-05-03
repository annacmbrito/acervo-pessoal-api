from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db_session
from src.routes.auth.main import get_current_user
from src.routes.users.schemas import CurrentUserResponse, SaveUserRequest
from src.routes.users.services import UserService

router = APIRouter(
    prefix="/api/v1/users", 
    tags=["Users"],
    responses={ 404: { "description": "Not found" } }
)

@router.get("/me")
def get_logged_user(user_email: str = Depends(get_current_user),
                    session: Session = Depends(get_db_session)):
    current_user = UserService(session).find_by_email(user_email)
    return CurrentUserResponse(
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        email=current_user.email
    )

@router.post("/", status_code=status.HTTP_201_CREATED)
def save_user(request: SaveUserRequest, session: Session = Depends(get_db_session)):
    return UserService(session).save(request.to_model())
