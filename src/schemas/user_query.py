from typing import Optional

from pydantic import BaseModel


class UserQuerySchema(BaseModel):
    id: int
    product: str
    quantity: float
    unit: str
    filter: Optional[str] = None
    user_id: int

    class Config:
        from_attributes = True


class UserQuerySchemaAdd(BaseModel):
    product: str
    quantity: float
    unit: str
    filter: Optional[str] = None
    user_id: Optional[int] = None
