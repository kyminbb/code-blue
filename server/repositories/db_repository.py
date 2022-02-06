from typing import List
from typing import Optional

from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from server.models.sections import Section
from server.models.visitors import Visitor
from server.schemas.visitors import Doctor


class DBRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def visitor_exists(self, name: str, section: int, seat: str) -> bool:
        statement = select((func.count())).where(Visitor.name == name and Visitor.section_seat == f"{section}_{seat}")
        result = await self.session.execute(statement)
        return result.first()[0] == 1

    async def add_visitor(self, name: str, section: int, seat: str, consent: bool, fcm_token: str) -> int:
        visitor = Visitor(
            name=name,
            section_seat=f"{section}_{seat}",
            section=section,
            consent=consent,
            fcm_token=fcm_token
        )
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

    async def update_token(self, visitor_id: int, fcm_token: str) -> int:
        statement = update(Visitor).where(Visitor.id == visitor_id).values(fcm_token=fcm_token)
        await self.session.execute(statement)
        try:
            await self.session.commit()
            return visitor_id
        except IntegrityError:
            await self.session.rollback()
            return -1

    async def get_gate(self, visitor_id: int) -> int:
        statement = select(Section.gate).join(
            Visitor,
            Visitor.section == Section.section
        ).where(Visitor.id == visitor_id)
        result = await self.session.execute(statement)
        return result.scalar()

    async def get_doctors(self) -> List[Doctor]:
        statement = select(Visitor.fcm_token, Section.section, Section.gate).join(
            Visitor,
            Visitor.section == Section.section
        ).where(Visitor.consent)
        result = await self.session.execute(statement)
        return result.fetchall()
