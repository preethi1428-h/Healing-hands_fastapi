from pydantic import BaseModel

class ProviderCreate(BaseModel):
    name: str
    specialization: str
    service_id: int

class ProviderResponse(BaseModel):
    id: int
    name: str
    specialization: str
    service_id: int

    model_config = {"from_attributes": True}
