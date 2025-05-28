from pydantic_settings  import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    BROKER_URL: str
    TESTING: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
