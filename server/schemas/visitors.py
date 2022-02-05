from pydantic import BaseModel


class Visitor(BaseModel):
    name: str
    section: str
    seat: str
    consent: bool


class RegisterResponse(BaseModel):
    visitor_id: int
