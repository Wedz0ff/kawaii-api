from httpx import AsyncClient
from src.app.config import Settings

settings = Settings()


async def get_current_weather(city: str) -> dict:
    """
    Fetch the current weather for a given city from the OpenWeather API.
    """
    if not settings.OPENWEATHERMAP_API_KEY:
        raise ValueError("OpenWeather API key is not set in the environment variables.")

    params = {
        "q": city,
        "appid": settings.OPENWEATHERMAP_API_KEY,
        "units": "metric",
    }

    async with AsyncClient() as client:
        response = await client.get(settings.OPENWEATHERMAP_API_URL, params=params)

        if response.status_code != 200:
            raise Exception(
                f"Error fetching weather data: {response.status_code} - {response.text}"
            )

        return response.json()
