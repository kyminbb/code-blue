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


class UpdateTokenRequest(BaseModel):
    visitor_id: int
    fcm_token: str


class VisitorResponse(BaseModel):
    visitor_id: int
