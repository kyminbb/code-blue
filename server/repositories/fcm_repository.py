from typing import List

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

from server.api.dependencies import get_settings


class FCMRepository:
    @classmethod
    def _initialize(cls) -> None:
        try:
            firebase_admin.get_app()
        except ValueError:
            cred = credentials.Certificate(get_settings().FIREBASE_CREDENTIALS)
            firebase_admin.initialize_app(cred)

    @classmethod
    async def send_message(cls, client_token: str) -> None:
        cls._initialize()
        message = messaging.Message(
            data={},
            token=client_token,
        )
        messaging.send(message)

    @classmethod
    async def multicast_message(cls, client_tokens: List[str]) -> None:
        cls._initialize()
        message = messaging.MulticastMessage(
            data={},
            tokens=client_tokens,
        )
        messaging.send_multicast(message)
