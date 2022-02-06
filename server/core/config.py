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

    DB_USER: str = os.getenv("POSTGRES_USER")
    DB_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    DB_HOST: str = os.getenv("POSTGRES_HOST")
    DB_PORT: int = int(os.getenv("POSTGRES_PORT"))
    DB_NAME: str = os.getenv("POSTGRES_DB")
    DB_URL: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    FIREBASE_CREDENTIALS: str = os.getenv("FIREBASE_CREDENTIALS")
    NOTIFICATION_TITLE: str = "EMERGENCY ALERT"
    DOCTOR_NOTIFICATION_BODY: str = "Heart attack occurred at section {0} seat {1}"
    ROW_NOTIFICATION_BODY: str = "Make way for the medical staff"
