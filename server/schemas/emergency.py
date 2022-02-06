from pydantic import BaseModel


class Emergency(BaseModel):
    visitor_id: int
    emergency_code: int


class DoctorMessage(BaseModel):
    emergency_code: int
    to_gate: int
    patient_section: int
    patient_seat: str
