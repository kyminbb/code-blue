import os
from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "code-blue"
    ALLOW_ORIGINS: List[str] = ["*"]

    DB_USER: str = os.getenv("DB_USER", "fabregas")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "vanpersie")
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "code_blue"
    DB_URL: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
