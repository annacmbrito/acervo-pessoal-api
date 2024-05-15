from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.config.database import get_db_session
from src.routes.books.schemas import SaveBookRequest
from src.routes.books.service import Book, BookService

router = APIRouter(
    prefix="/api/v1/books", 
    tags=["Books"],
    responses={ 404: { "description": "Not found" } }
)

@router.get("/")
def find_all(page: Page = Depends(), session: Session = Depends(get_db_session)):
    return BookService(session).find_all(page)

@router.get("/{id}")
def find_by_id(id: int, session: Session = Depends(get_db_session)):
    return BookService(session).filter(Book.id == id).first()

@router.post("/", status_code=status.HTTP_201_CREATED)
def save_user(request: SaveBookRequest, session: Session = Depends(get_db_session)):
    return BookService(session).save(request)

@router.put("/{id}")
def update_by_id(id: int, 
                 request: SaveBookRequest,
                 session: Session = Depends(get_db_session)):
    BookService(session).update_by_id(id, request.to_model())

@router.delete("/{id}")
def delete_by_id(id: int, session: Session = Depends(get_db_session)):
    BookService(session).delete_by_id(id)
