from pydantic import BaseModel


class Emergency(BaseModel):
    visitor_id: int
    emergency_code: int
