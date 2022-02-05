from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Visitor(Base):
    __tablename__ = "visitors_info"

    #Add Token Column
    id = Column(Integer,primary_key=True)
    name = Column(String)
    section_seat = Column(String, unique=True)
    section = Column(String)
    is_doctor = Column(Boolean)

    def __str__(self):
        return f"{self.name.strip()}//{self.section_seat.strip()}//{self.is_doctor}//"


