from typing import Optional

from server.repositories.visitors_repository import VisitorsRepository
from server.schemas.visitors import RegisterResponse
from server.schemas.visitors import Visitor


class VisitorsService:
    def __init__(self, visitors_repository: VisitorsRepository):
        self.visitors_repository = visitors_repository

    async def register_visitor(self, visitor: Visitor) -> RegisterResponse:
        visitor_id = -1
        if not await self.visitors_repository.visitor_exists(visitor.name, visitor.section, visitor.seat):
            visitor_id = await self.visitors_repository.add_visitor(
                visitor.name,
                visitor.section,
                visitor.seat,
                visitor.consent
            )
        return RegisterResponse(visitor_id=visitor_id)

    async def get_visitor(self, visitor_id: int) -> Optional[Visitor]:
        visitor = await self.visitors_repository.get_isitor(visitor_id)
        if not visitor:
            return None
        section_seat = visitor.section_seat.split("_")
        return Visitor(name=visitor.name, section=section_seat[0], seat=section_seat[1], consent=visitor.consent)
