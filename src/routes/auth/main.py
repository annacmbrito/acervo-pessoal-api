from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)