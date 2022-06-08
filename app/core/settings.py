from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str  # postgres
    USERS_TABLE_NAME: str = 'users'
    TORTOISE_MODELS: list = ['app.core.models.users']

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings():
    return Settings()
