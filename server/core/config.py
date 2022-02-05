from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "code-blue"
    ALLOW_ORIGINS: List[str] = []
