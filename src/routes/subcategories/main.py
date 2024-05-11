from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.config.database import get_db_session
from src.routes.subcategories.schemas import *
from src.routes.subcategories.service import SubcategoryService

router = APIRouter(
    prefix="/api/v1/subcategories", 
    tags=["Subcategories"],
    responses={ 404: { "description": "Not found" } }
)

@router.get("/")
def find_all(filter: SubcategoryFilter = Depends(), 
             page: Page = Depends(), 
             session: Session = Depends(get_db_session)):
    return SubcategoryService(session).find_all(filter, page)

@router.post("/", status_code=status.HTTP_201_CREATED)
def save_user(request: SaveSubcategoryRequest, session: Session = Depends(get_db_session)):
    return SubcategoryService(session).save(request.to_model())