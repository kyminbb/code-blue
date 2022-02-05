from functools import lru_cache
from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from server.core.config import Settings
from server.repositories.visitors_repository import VisitorsRepository
from server.services.visitors_service import VisitorsService


@lru_cache()
def get_settings() -> Settings:
    return Settings()


engine = create_async_engine(get_settings().DB_URL)


async def close_db() -> None:
    await engine.dispose()


@lru_cache()
def _get_reusable_session_maker() -> sessionmaker:
    return sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session_maker() -> AsyncGenerator[sessionmaker, None]:
    yield _get_reusable_session_maker()


def get_visitors_repository(session_maker: sessionmaker = Depends(get_session_maker)) -> VisitorsRepository:
    return VisitorsRepository(session_maker)


def get_visitors_service(visitors_repository: VisitorsRepository = Depends(get_visitors_repository)) -> VisitorsService:
    return VisitorsService(visitors_repository)
