from pydantic import BaseModel


class Visitor(BaseModel):
    name: str
    section: int
    seat: str
    consent: bool
    fcm_token: str


class Doctor(BaseModel):
    section: int
    gate: int
    fcm_token: str


class RegisterResponse(BaseModel):
    visitor_id: int
