from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URL: str
    CHANNEL_ID: int
    BOT_TOKEN: str
    WEBAPP_URL: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()