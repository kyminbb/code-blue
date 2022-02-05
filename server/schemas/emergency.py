from pydantic import BaseModel


class Emergency(BaseModel):
    visitor_id: str
    emergency_code: int
