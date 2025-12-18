from pydantic import BaseModel

class ServiceCreate(BaseModel):
    title: str
    description: str
    icon: str | None = None


class ServiceUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    icon: str | None = None


class ServiceResponse(BaseModel):
    id: int
    title: str
    description: str
    icon: str | None = None
    
    model_config = {
        "from_attributes": True
    }

