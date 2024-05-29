from fastapi import APIRouter, Depends, status, File, UploadFile
from sqlalchemy.orm import Session
from src.config.database import get_db_session
from src.routes.images.client import ImageKitClient
from src.routes.images.service import ImageService

router = APIRouter(
    prefix="/api/v1/images", 
    tags=["Images"],
    responses={ 404: { "description": "Not found" } }
)

@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def save_user(file: UploadFile = File(...), session: Session = Depends(get_db_session)):
    image = await ImageKitClient().upload(file)
    return ImageService(session).save(image)