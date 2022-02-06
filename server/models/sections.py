from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from server.models import Base


class Section(Base):
    __tablename__ = "sections"

    section = Column(Integer, primary_key=True)
    gate = Column(Integer)
    neighbors = Column(String)
