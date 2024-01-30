from typing import Optional

from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    title: str
    price: float
    image: str
    href: str
    description: Optional[str] = None
    market_id: Optional[int] = None
    user_query_id: Optional[int] = None

    class Config:
        from_attributes = True


class ProductSchemaAdd(BaseModel):
    title: str
    price: float
    image: str
    href: str
    description: Optional[str] = None
    market_id: Optional[int] = None
    user_query_id: Optional[int] = None
