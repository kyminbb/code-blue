from typing import Optional

from server.schemas.visitors import RegisterResponse
from server.schemas.visitors import Visitor


class VisitorsService:
    async def register_visitor(self, visitor: Visitor) -> RegisterResponse:
        return RegisterResponse(visitor_id=1)

    async def get_visitor(self, visitor_id: int) -> Optional[Visitor]:
        return Visitor(name="Sebeom Lee", section="A", seat="K2", consent=True)
