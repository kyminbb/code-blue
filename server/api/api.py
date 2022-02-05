from fastapi import APIRouter

from server.api.endpoints import health

api_router = APIRouter(prefix="/api")
api_router.include_router(health.router)
