from functools import lru_cache

from fastapi import FastAPI
from fastapi.params import Depends
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Annotated

from app import config


class Settings(BaseSettings):
    """application settings"""

    app_name: str = "Awesome API"
    admin_email: str = "admin@test.com"
    items_per_user: int = 50

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    """get settings"""
    return config.Settings()


app = FastAPI()


@app.get("/info")
async def info(settings: Annotated[config.Settings, Depends(get_settings)]):
    """handler function for info path"""
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }
