from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENWEATHERMAP_API_URL: str
    OPENWEATHERMAP_API_KEY: str
    OPENAI_API_KEY: str
    OPENAI_API_URL: str

    class Config:
        env_file = ".env"
