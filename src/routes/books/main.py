from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.config.database import get_db_session
from src.routes.books.schemas import *
from src.routes.books.service import BookService

router = APIRouter(
    prefix="/api/v1/books", 
    tags=["Books"],
    responses={ 404: { "description": "Not found" } }
)

@router.get("/")
def find_all(page: Page = Depends(), 
             filter: BookFilter = Depends(), 
             session: Session = Depends(get_db_session)):
    return BookService(session).find_all(filter, page)

@router.get("/{id}")
def find_by_id(id: int, session: Session = Depends(get_db_session)):
    return BookService(session).find_by_id(id)

@router.post("/", status_code=status.HTTP_201_CREATED)
def save_user(request: SaveBookRequest, session: Session = Depends(get_db_session)):
    return BookService(session).save(request)

@router.put("/{id}")
def update_by_id(id: int, 
                 request: SaveBookRequest,
                 session: Session = Depends(get_db_session)):
    BookService(session).update_by_id(id, request)

@router.delete("/{id}")
def delete_by_id(id: int, session: Session = Depends(get_db_session)):
    BookService(session).delete_by_id(id)
