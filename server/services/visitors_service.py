from server.schemas.visitors import RegisterResponse
from server.schemas.visitors import Visitor


class VisitorsService:
    async def register_visitor(self, visitor: Visitor) -> RegisterResponse:
        return RegisterResponse(visitor_id=1)
