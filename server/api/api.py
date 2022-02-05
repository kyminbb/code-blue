from fastapi import APIRouter

from server.api.endpoints import emergency
from server.api.endpoints import health
from server.api.endpoints import visitors

api_router = APIRouter(prefix="/api")
api_router.include_router(health.router)
api_router.include_router(visitors.router)
api_router.include_router(emergency.router)
