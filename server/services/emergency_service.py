from server.repositories.fcm_repository import FCMRepository
from server.repositories.visitors_repository import VisitorsRepository
from server.schemas.emergency import Emergency


class EmergencyService:
    def __init__(self, visitors_repository: VisitorsRepository, fcm_repository: FCMRepository):
        self.visitors_repository = visitors_repository
        self.fcm_repository = fcm_repository

    async def handle_emergency(self, emergency: Emergency) -> None:
        pass
