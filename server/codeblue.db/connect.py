
import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from visitor import *
from service import *

USER = "fabregas"
PASSWORD = "vanpersie"
DB_NAME = "code_blue"
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@localhost:5432/{DB_NAME}"

Base = declarative_base()
engine = create_async_engine(SQLALCHEMY_DATABASE_URL,echo=True)
async_session = sessionmaker(engine, class_ = AsyncSession, expire_on_commit=False)

#Add Visitor
async def add_visitor(session : AsyncSession,name : str, section : str, seat : str, isDoctor : bool):
    return await add_visitor_help(session,name,section,seat,isDoctor)

#Get Visitor Row
async def get_visitor_info(session, id : int):
    return await get_visitor_info_help(session,id)

#Testing
async def test():
    async with async_session() as session:
        # await add_visitor(session,"Leo Jung","2","F82",True)
        # await add_visitor(session, "Caleb Drexel", "5", "F21", True)
        # print("Passed 2!")
        # await add_visitor(session, "Michael Phelps", "2", "K23", False)
        # print("Passed 3!")
        result = await get_visitor_info(session,3)
        print(result)
        return result