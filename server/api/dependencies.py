from functools import lru_cache

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from server.core.config import Settings
from server.models import Base
from server.repositories.visitors_repository import VisitorsRepository
from server.services.visitors_service import VisitorsService


@lru_cache()
def get_settings() -> Settings:
    return Settings()


engine: AsyncEngine = create_async_engine(get_settings().DB_URL, future=True)
session_maker: sessionmaker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def start_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def shutdown_db() -> None:
    await engine.dispose()


async def get_session() -> AsyncSession:
    async with session_maker() as session:
        yield session


def get_visitors_repository(session: AsyncSession = Depends(get_session)) -> VisitorsRepository:
    return VisitorsRepository(session)


def get_visitors_service(visitors_repository: VisitorsRepository = Depends(get_visitors_repository)) -> VisitorsService:
    return VisitorsService(visitors_repository)
