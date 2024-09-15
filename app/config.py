from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """application settings"""

    app_name: str = "Awesome API"
    admin_email: str = "admin@test.com"
    items_per_user: int = 50

    model_config = SettingsConfigDict(env_file=".env")
