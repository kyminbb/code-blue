import os
import sys
from typing import List

from dotenv import load_dotenv
from pydantic import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)


class Settings(BaseSettings):
    APP_NAME: str = "code-blue"
    ALLOW_ORIGINS: List[str] = ["*"]

    DB_URL: str = os.getenv("DB_URL")

