from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.config.database import get_db_session
from src.routes.publishers.schemas import SavePublisherRequest
from src.routes.publishers.service import PublisherService

router = APIRouter(
    prefix="/api/v1/publishers", 
    tags=["Publishers"],
    responses={ 404: { "description": "Not found" } }
)

@router.get("/")
def find_all(page: Page = Depends(), session: Session = Depends(get_db_session)):
    return PublisherService(session).find_all(page)

@router.post("/", status_code=status.HTTP_201_CREATED)
def save_user(request: SavePublisherRequest, session: Session = Depends(get_db_session)):
    return PublisherService(session).save(request.to_model())

@router.delete("/{id}")
def delete_by_id(id: int, session: Session = Depends(get_db_session)):
    PublisherService(session).delete_by_id(id)