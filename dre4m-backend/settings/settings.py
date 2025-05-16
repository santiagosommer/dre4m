# Imports
import os

# From imports
from functools import lru_cache
from pydantic import field_validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # .env values
    ENVIRONMENT: str = ""
    DATABASE_URL: str = ""
    DB_NAME: str = ""
    DB_USER: str = ""
    DB_USER_PASSWORD: str = ""
    DB_HOST: str = ""
    DB_PORT: int = 0000
    DEFAULT_DB_USER: str = ""
    TEST_DB_NAME: str = ""
    LOG_LEVEL: str = ""
    SECRET_KEY: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 0

    # Properties
    @property
    def IS_PRODUCTION(self) -> bool:
        return self.ENVIRONMENT.lower() == "production"

    # @property
    # def COOKIE_SECURE(self) -> bool:
    #     return self.IS_PRODUCTION

    # COOKIE_SAMESITE: str = "strict"
    # COOKIE_HTTPONLY: bool = True

    # Validations
    @field_validator("ENVIRONMENT")
    def check_environment(cls, v: str) -> str:
        allowed = {'development', 'production'}
        if v.lower() not in allowed:
            raise ValueError(f"ENVIRONMENT must be one of {allowed}")
        return v

    @field_validator("SECRET_KEY")
    def check_secret_key(cls, v: str) -> str:
        if not v and os.getenv("ENVIRONMENT", "").lower() != "production":
            raise ValueError("SECRET_KEY must be set for production")
        return v


@lru_cache
def get_settings() -> Settings:
    return Settings()
