from fastapi import APIRouter, HTTPException
from src.app.services.weather_service import get_current_weather
from fastapi_cache.decorator import cache

router = APIRouter()


@cache(expire=60 * 2)  # 2 minutes
@router.get("/weather")
async def fetch_weather(city: str):
    try:
        weather_data = await get_current_weather(city)
        return weather_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
