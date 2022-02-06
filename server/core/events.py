from typing import Any
from typing import Callable

from fastapi import FastAPI

from server.api.dependencies import shutdown_db
from server.api.dependencies import start_db


def create_start_app_handler(app: FastAPI) -> Callable[..., Any]:
    async def start_app() -> None:
        await start_db()

    return start_app


def create_shutdown_app_handler(app: FastAPI) -> Callable[..., Any]:
    async def shutdown_app() -> None:
        await shutdown_db()

    return shutdown_app
