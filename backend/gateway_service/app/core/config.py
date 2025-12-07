from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MONGODB_URL: str
    AUTH_SERVICE_BASEURL: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
