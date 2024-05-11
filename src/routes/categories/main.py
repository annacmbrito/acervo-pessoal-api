from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/categories", 
    tags=["Categories"],
    responses={ 404: { "description": "Not found" } }
)