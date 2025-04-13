from fastapi import APIRouter
from .weather import router as weather
from .words import router as words
from .curiosities import router as curiosities

api_router = APIRouter()


api_router.include_router(weather)
api_router.include_router(words)
api_router.include_router(curiosities)
