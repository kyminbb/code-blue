from typing import List
from typing import Optional

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

    async def send_message(self, client_token: str, data: Optional[DoctorMessage] = None) -> None:
        self._initialize()
        message_data = {k: str(v) for k, v in data.__dict__.items()} if data else {}
        body = self.settings.DOCTOR_NOTIFICATION_BODY.format(
            data.patient_section,
            data.patient_seat
        ) if data else self.settings.ROW_NOTIFICATION_BODY
        message = messaging.Message(
            notification=messaging.Notification(
                title=self.settings.NOTIFICATION_TITLE,
                body=body
            ),
            data=message_data,
            token=client_token
        )
        try:
            messaging.send(message)
        except messaging.UnregisteredError:
            # TODO: Delete visitor_id from DB
            pass

    async def multicast_message(self, client_tokens: List[str], data: Optional[DoctorMessage] = None) -> None:
        self._initialize()
        message_data = {k: str(v) for k, v in data.__dict__.items()} if data else {}
        body = self.settings.DOCTOR_NOTIFICATION_BODY.format(
            data.patient_section,
            data.patient_seat
        ) if data else self.settings.ROW_NOTIFICATION_BODY
        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title=self.settings.NOTIFICATION_TITLE,
                body=body
            ),
            data=message_data,
            tokens=list(set(client_tokens))
        )
        try:
            messaging.send_multicast(message)
        except messaging.UnregisteredError:
            # TODO: Delete visitor_id from DB
            pass
