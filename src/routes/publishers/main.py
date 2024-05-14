from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/publishers", 
    tags=["Publishers"],
    responses={ 404: { "description": "Not found" } }
)