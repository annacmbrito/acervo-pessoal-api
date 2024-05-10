from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/authors", 
    tags=["Authors"],
    responses={ 404: { "description": "Not found" } }
)