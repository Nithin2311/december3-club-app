"""Runtime configuration, loaded from environment variables."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+asyncpg://dec3:dec3@db:5432/dec3"
    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.5-flash"
    session_secret: str = "dev-insecure-change-me"
    cookie_secure: bool = True
    cors_origins: str = "http://localhost"

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


settings = Settings()
