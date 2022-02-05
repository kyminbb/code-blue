from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from server.models import Base

class GateSection(Base):

    __tablename__ = "gate_section"

    gate = Column(String)
    section = Column(String,primary_key=True)
    
