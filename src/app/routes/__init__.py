from fastapi import APIRouter
from .weather import router as weather
from .words import router as words
from .curiosities import router as curiosities
from .root import router as root

api_router = APIRouter()


api_router.include_router(root)
api_router.include_router(curiosities)
api_router.include_router(weather)
api_router.include_router(words)
