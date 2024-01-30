from sqlalchemy import ForeignKey

from src.db.db import Base
from sqlalchemy.orm import Mapped, mapped_column

from src.schemas.user import UserSchema
from src.schemas.user_query import UserQuerySchema


class UserQuery(Base):
    __tablename__ = 'user_queries'
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    product: Mapped[str]
    quantity: Mapped[float]
    unit: Mapped[str]
    filter: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'))

    def to_read_model(self) -> UserQuerySchema:
        return UserQuerySchema(
            id=self.id,
            product=self.product,
            quantity=self.quantity,
            unit=self.unit,
            filter=self.filter,
            user_id=self.user_id
        )
