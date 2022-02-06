from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.api.api import api_router
from server.api.dependencies import get_settings
from server.core.events import create_shutdown_app_handler
from server.core.events import create_start_app_handler

settings = get_settings()

app = FastAPI(title=settings.APP_NAME)
app.add_event_handler("startup", create_start_app_handler(app))
app.add_event_handler("shutdown", create_shutdown_app_handler(app))
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
