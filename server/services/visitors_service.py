from typing import Optional

from server.repositories.db_repository import DBRepository
from server.schemas.visitors import UpdateTokenRequest
from server.schemas.visitors import Visitor
from server.schemas.visitors import VisitorResponse


class VisitorsService:
    def __init__(self, db_repository: DBRepository):
        self.db_repository = db_repository

    async def register_visitor(self, visitor: Visitor) -> VisitorResponse:
        visitor_id = -1
        gate = -1
        if not await self.db_repository.visitor_exists(visitor.name, visitor.section, visitor.seat):
            visitor_id = await self.db_repository.add_visitor(
                visitor.name,
                visitor.section,
                visitor.seat,
                visitor.consent,
                visitor.fcm_token,
            )
            gate = await self.db_repository.get_gate(visitor_id)
        return VisitorResponse(visitor_id=visitor_id, gate=gate)

    async def get_visitor(self, visitor_id: int) -> Optional[Visitor]:
        visitor = await self.db_repository.get_visitor(visitor_id)
        if not visitor:
            return None
        return Visitor(
            name=visitor.name,
            section=visitor.section,
            seat="".join(visitor.section_seat.split("_")[1:]),
            consent=visitor.consent,
            fcm_token=visitor.fcm_token
        )

    async def update_token(self, update_token_request: UpdateTokenRequest) -> VisitorResponse:
        visitor_id = await self.db_repository.update_token(
            update_token_request.visitor_id,
            update_token_request.fcm_token
        )
        return VisitorResponse(visitor_id=visitor_id)
