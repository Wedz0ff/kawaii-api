from fastapi import APIRouter
from fastapi_cache.decorator import cache

from src.app.services.curiosities_service import generate_curiosity, CuriosityRequest

router = APIRouter()


@router.get("/random-curiosity")
@cache(expire=60 * 60 * 6)  # 6 hours
async def fetch_curiosity():
    request = CuriosityRequest()
    return await generate_curiosity(request)
