from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from visitor import *

def check_dup_visitor(section,seat,name):
    return select((func.count())).where(Visitor.name == name and section_seat == f"{section}_{seat}")

# Add new visitor to db
async def add_visitor_help(session: AsyncSession,name : str, section : str,seat : str,isDoctor):
    check_stmt = check_dup_visitor(section, seat, name)
    is_duplicate = await session.execute(check_stmt)
    if is_duplicate.first()[0] != 1:
        print("Checked Duplicate")
        #not in the table
        new_visitor = Visitor(name=name,section_seat=f"{section}_{seat}",section=section,is_doctor=isDoctor)
        session.add(new_visitor)
        try:
            await session.commit()
            return new_visitor.id
        except:
            await session.rollback()
            raise DuplicatedEntryError("The Visitor Already Exists")

#Get visitor row using their name and their seat
async def get_visitor_info_help(session: AsyncSession, id : int):
    result = await session.execute(select(Visitor).where(Visitor.id == id))
    return result.scalar()
