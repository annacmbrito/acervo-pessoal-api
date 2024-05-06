from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/books", 
    tags=["Books"],
    responses={ 404: { "description": "Not found" } }
)
