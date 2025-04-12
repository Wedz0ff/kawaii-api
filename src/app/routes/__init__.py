from fastapi import APIRouter
from .weather import router as weather

api_router = APIRouter()


api_router.include_router(weather, tags=["weather"])
