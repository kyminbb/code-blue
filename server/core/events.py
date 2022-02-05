from typing import Any
from typing import Callable

from fastapi import FastAPI

from server.api.dependencies import _get_reusable_session_maker
from server.api.dependencies import close_db


def create_start_app_handler(app: FastAPI) -> Callable[..., Any]:
    async def start_app() -> None:
        _get_reusable_session_maker()

    return start_app


def create_shutdown_app_handler(app: FastAPI) -> Callable[..., Any]:
    async def shutdown_app() -> None:
        await close_db()

    return shutdown_app
