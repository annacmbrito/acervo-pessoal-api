from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.config.database import get_db_session
from src.routes.categories.schemas import SaveCategoryRequest
from src.routes.categories.service import CategoryService

router = APIRouter(
    prefix="/api/v1/categories", 
    tags=["Categories"],
    responses={ 404: { "description": "Not found" } }
)

@router.get("/")
def find_all(page: Page = Depends(), session: Session = Depends(get_db_session)):
    return CategoryService(session).find_all(page)

@router.post("/", status_code=status.HTTP_201_CREATED)
def save_user(request: SaveCategoryRequest, session: Session = Depends(get_db_session)):
    return CategoryService(session).save(request.to_model())

@router.delete("/{id}")
def delete_by_id(id: int, session: Session = Depends(get_db_session)):
    CategoryService(session).delete_by_id(id)