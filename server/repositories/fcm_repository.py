from typing import List
from typing import Union

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

from server.core.config import Settings
from server.schemas.emergency import DoctorMessage


class FCMRepository:
    def __init__(self, settings: Settings):
        self.settings = settings

    def _initialize(self) -> None:
        try:
            firebase_admin.get_app()
        except ValueError:
            cred = credentials.Certificate(self.settings.FIREBASE_CREDENTIALS)
            firebase_admin.initialize_app(cred)

    async def send_message(self, client_token: str, data: Union[DoctorMessage]) -> None:
        self._initialize()
        message = messaging.Message(data=data.__dict__, token=client_token)
        messaging.send(message)

    async def multicast_message(self, client_tokens: List[str], data: Union[DoctorMessage]) -> None:
        self._initialize()
        message = messaging.MulticastMessage(data=data.__dict__, tokens=client_tokens)
        messaging.send_multicast(message)