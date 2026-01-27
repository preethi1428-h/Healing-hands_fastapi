from pydantic import BaseModel
from typing import Optional

class AppointmentCreate(BaseModel):
    name: str
    phone: str
    email:str
    date: str
    time: str
    service: str
    additional:str
    user_id: int
    provider_id: int  
    counselor_name: Optional[str] = None




class AppointmentResponse(BaseModel):
    id: int
    name: str
    email:str
    phone: str
    date: str
    time: str
    service: str
    additional:Optional[str]=None
    status: str 
    counselor_name: Optional[str] = None
    user_id: Optional[int] = None
    provider_id: int | None = None


    model_config = {"from_attributes": True}

