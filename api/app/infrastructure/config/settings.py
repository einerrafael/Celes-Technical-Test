from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    FIREBASE_WEB_API_KEY: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"


environment_settings = Settings()
