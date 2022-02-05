from typing import Optional

from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from server.models.visitors import Visitor


class VisitorsRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def visitor_exists(self, name: str, section: str, seat: str) -> bool:
        statement = select((func.count())).where(Visitor.name == name and Visitor.section_seat == f"{section}_{seat}")
        result = await self.session.execute(statement)
        return result.first()[0] == 1

    async def add_visitor(self, name: str, section: str, seat: str, consent: bool) -> int:
        visitor = Visitor(name=name, section_seat=f"{section}_{seat}", section=section, consent=consent)
        self.session.add(visitor)
        try:
            await self.session.commit()
            return visitor.id
        except IntegrityError:
            await self.session.rollback()
            return -1


async def get_visitor(self, visitor_id: int) -> Optional[Visitor]:
    result = await self.session.execute(select(Visitor).where(Visitor.id == visitor_id))
    return result.scalar()
