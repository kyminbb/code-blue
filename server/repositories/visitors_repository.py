from typing import Optional

from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import sessionmaker

from server.model.gate_section import GateSection
from server.model.visitor import Visitor


class VisitorsRepository:
    def __init__(self, session_maker: sessionmaker):
        self.async_session = session_maker

    async def visitor_exists(self, name: str, section: str, seat: str) -> bool:
        statement = select((func.count())).where(Visitor.name == name and Visitor.section_seat == f"{section}_{seat}")
        async with self.async_session() as session:
            return await session.execute(statement).first()[0] == 1

    async def add_visitor(self, name: str, section: str, seat: str, consent: bool) -> int:
        visitor = Visitor(name=name, section_seat=f"{section}_{seat}", section=section, consent=consent)
        async with self.async_session() as session:
            session.add(visitor)
            try:
                await session.commit()
                return visitor.id
            except IntegrityError:
                await session.rollback()
                return -1

    async def get_visitor(self, visitor_id: int) -> Optional[Visitor]:
        async with self.async_session() as session:
            result = await session.execute(select(Visitor).where(Visitor.id == visitor_id))
            return result.scalar()

    async def get_gate(self, visitor_id : int) -> str:
        async with self.async_session() as session:
            result = await session.execute(select(GateSection.gate).join(Visitor,
                                                                         Visitor.section == GateSection.section)
                                           .where(Visitor.id == visitor_id))
            return result.scalar()

    async def get_doctors(self) -> Optional[Visitor]:
        async with self.async_session() as session:
            result = await session.execute(select(Visitor.id,GateSection.section,GateSection.gate).
                                           join(Visitor,Visitor.section == GateSection.section)
                                           .where(Visitor.consent == True))
            return result.scalars()