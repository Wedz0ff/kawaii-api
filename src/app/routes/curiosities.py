from fastapi import APIRouter
from fastapi_cache.decorator import cache

from src.app.services.curiosities_service import generate_curiosity, CuriosityRequest

router = APIRouter()


@router.post("/random-curiosity")
@cache(expire=60 * 60 * 6)  # 6 hours
async def fetch_curiosity(theme: str | None = None):
    """
    Fetch a random curiosity based on the provided theme and detail level.
    """
    # Create a CuriosityRequest object
    request = CuriosityRequest(theme=theme)
    return await generate_curiosity(request)
