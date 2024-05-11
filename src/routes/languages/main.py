from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/languages", 
    tags=["Languages"],
    responses={ 404: { "description": "Not found" } }
)