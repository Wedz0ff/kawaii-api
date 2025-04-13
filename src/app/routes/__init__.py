from fastapi import APIRouter
from .weather import router as weather
from .words import router as words

api_router = APIRouter()


api_router.include_router(weather)
api_router.include_router(words)
