from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.config.database import get_db_session
from src.routes.authors.schemas import SaveAuthorRequest
from src.routes.authors.services import AuthorService

router = APIRouter(
    prefix="/api/v1/authors", 
    tags=["Authors"],
    responses={ 404: { "description": "Not found" } }
)

@router.get("/")
def find_all(page: Page, session: Session = Depends(get_db_session)):
    return AuthorService(session).find_all(page)

@router.post("/", status_code=status.HTTP_201_CREATED)
def save_user(request: SaveAuthorRequest, session: Session = Depends(get_db_session)):
    return AuthorService(session).save(request.to_model())