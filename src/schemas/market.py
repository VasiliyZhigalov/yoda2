from pydantic import BaseModel


class MarketSchema(BaseModel):
    id: int
    name: str
    number: str
    href: str

    class Config:
        from_attributes = True


class MarketSchemaAdd(BaseModel):
    name: str
    number: str
    href: str
