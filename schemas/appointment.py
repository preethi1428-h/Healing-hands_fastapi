from pydantic import BaseModel

class AppointmentCreate(BaseModel):
    name: str
    phone: str
    date: str
    time: str
    service: str
    user_id: int


class AppointmentResponse(BaseModel):
    id: int
    name: str
    phone: str
    date: str
    time: str
    service: str
    user_id: int
    status: str  

    model_config = {"from_attributes": True}
