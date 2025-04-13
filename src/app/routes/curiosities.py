from fastapi import APIRouter
from src.app.services.curiosities_service import generate_curiosity, CuriosityRequest

router = APIRouter()


@router.post("/random-curiosity")
async def fetch_curiosity(theme: str | None = None, detail_level: str = "high"):
    """
    Fetch a random curiosity based on the provided theme and detail level.
    """
    # Create a CuriosityRequest object
    request = CuriosityRequest(theme=theme, detail_level=detail_level)
    return await generate_curiosity(request)
