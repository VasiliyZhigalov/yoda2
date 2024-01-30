from sqlalchemy import ForeignKey
from src.db.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from src.schemas.product import ProductSchema


class Product(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    title: Mapped[str]
    price: Mapped[float]
    image: Mapped[str]
    href: Mapped[str]
    description: Mapped[str]
    market_id: Mapped[int] = mapped_column(ForeignKey('markets.id'))
    user_query_id: Mapped[int] = mapped_column(ForeignKey('user_queries.id'))

    def to_read_model(self) -> ProductSchema:
        return ProductSchema(
            id=self.id,
            title=self.title,
            price=self.price,
            image=self.image,
            href=self.href,
            market_id=self.market_id,
            user_query_id=self.user_query_id
        )
