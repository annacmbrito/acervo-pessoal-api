from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/subcategories", 
    tags=["Subcategories"],
    responses={ 404: { "description": "Not found" } }
)