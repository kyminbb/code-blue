from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from server.models import Base


class Visitor(Base):
    __tablename__ = "visitors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    section_seat = Column(String, unique=True)
    section = Column(String)
    consent = Column(Boolean)
