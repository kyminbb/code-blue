from functools import lru_cache

from server.core.config import Settings


@lru_cache()
def get_settings() -> Settings:
    return Settings()