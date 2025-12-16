from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SENDER_ADDRESS: str
    SENDER_PASSWORD: str
    MP3_QUEUE: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
