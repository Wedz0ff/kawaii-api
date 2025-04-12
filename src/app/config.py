from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENWEATHERMAP_API_URL: str
    OPENWEATHERMAP_API_KEY: str

    class Config:
        env_file = ".env"  # Load environment variables from .env
