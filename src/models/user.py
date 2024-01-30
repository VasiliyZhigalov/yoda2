from src.db.db import Base
from sqlalchemy.orm import Mapped, mapped_column

from src.schemas.user import UserSchema


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    user_id: Mapped[int]
    name: Mapped[str]
    role: Mapped[str]
    latitude: Mapped[str]
    longitude: Mapped[str]

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            user_id=self.user_id,
            name=self.name,
            role=self.role,
            latitude=self.latitude,
            longitude=self.longitude

        )
