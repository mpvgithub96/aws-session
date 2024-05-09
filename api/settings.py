from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    QUEUE_URL: str
    TOPIC_ARN: str
    model_config = SettingsConfigDict(env_file=".env")
