import firebase_admin
from firebase_admin import credentials

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
