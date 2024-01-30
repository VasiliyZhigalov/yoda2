from pydantic import BaseModel, ConfigDict
from typing import Optional


class UserSchema(BaseModel):
    id: int
    user_id: int
    name: str
    role: str
    latitude: Optional[str] = None
    longitude: Optional[str] = None

    class Config:
        from_attributes = True


class UserSchemaAdd(BaseModel):
    user_id: int
    name: str
    role: str
    latitude: Optional[str] = None
    longitude: Optional[str] = None

    class Config:
        from_attributes = True
