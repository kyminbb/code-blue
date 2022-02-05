from functools import lru_cache

from server.core.config import Settings
from server.services.visitors_service import VisitorsService


@lru_cache()
def get_settings() -> Settings:
    return Settings()


def get_visitors_service() -> VisitorsService:
    return VisitorsService()
