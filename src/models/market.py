from sqlalchemy import ForeignKey
from src.db.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from src.schemas.market import MarketSchema


class Market(Base):
    __tablename__ = 'markets'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    number: Mapped[str]
    href: Mapped[str]

    def to_read_model(self) -> MarketSchema:
        return MarketSchema(
            id=self.id,
            name=self.name,
            number=self.number,
            href=self.href,
        )
