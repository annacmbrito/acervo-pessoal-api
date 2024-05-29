from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/images", 
    tags=["Images"],
    responses={ 404: { "description": "Not found" } }
)