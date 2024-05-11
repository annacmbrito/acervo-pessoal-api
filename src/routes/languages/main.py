from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.config.database import get_db_session
from src.routes.languages.service import LanguageService

router = APIRouter(
    prefix="/api/v1/languages", 
    tags=["Languages"],
    responses={ 404: { "description": "Not found" } }
)

@router.get("/")
def find_all(page: Page = Depends(), session: Session = Depends(get_db_session)):
    return LanguageService(session).find_all(page)