from typing import List
from typing import Optional
from typing import Tuple

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

    @classmethod
    def _get_row_col(cls, seat: str) -> Tuple[str, str]:
        col_idx = 0
        for i, c in enumerate(seat):
            if c.isdigit():
                col_idx = i
                break
        return seat[:col_idx], seat[col_idx:]

    async def visitor_exists(self, name: str, section: int, seat: str) -> bool:
        row, col = self._get_row_col(seat)
        statement = select((func.count())).where(
            Visitor.name == name and Visitor.section_seat == f"{section}_{row}_{col}"
        )
        result = await self.session.execute(statement)
        return result.first()[0] == 1

    async def add_visitor(self, name: str, section: int, seat: str, consent: bool, fcm_token: str) -> int:
        row, col = self._get_row_col(seat)
        visitor = Visitor(
            name=name,
            section_seat=f"{section}_{row}_{col}",
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

    async def get_visitor_row(self, visitor_id: int) -> str:
        statement = select(Visitor.section_seat).where(Visitor.id == visitor_id)
        result = await self.session.execute(statement)
        row = result.scalar().split("_")
        gate_section = row[0] + "_" + row[1] + "_"
        return gate_section

    async def get_row_tokens(self, visitor_id: int) -> List[str]:
        location = await self.get_visitor_row(visitor_id)
        statement = select(Visitor.fcm_token).filter(
            Visitor.id != visitor_id
        ).where(Visitor.section_seat.startswith(location))
        result = await self.session.execute(statement)
        return list(map(lambda row: row[0], result.fetchall()))
