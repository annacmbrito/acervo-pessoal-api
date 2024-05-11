from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db_session
from src.routes.books.schemas import SaveBookRequest
from src.routes.books.service import BookService

router = APIRouter(
    prefix="/api/v1/books", 
    tags=["Books"],
    responses={ 404: { "description": "Not found" } }
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def save_user(request: SaveBookRequest, session: Session = Depends(get_db_session)):
    return BookService(session).save(request.to_model())
