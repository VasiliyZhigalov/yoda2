from src.models.user_query import UserQuery
from src.repositories.repository import SQLAlchemyRepository


class UserQueryRepository(SQLAlchemyRepository):
    model = UserQuery
