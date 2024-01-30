from src.models.market import Market
from src.repositories.repository import SQLAlchemyRepository


class MarketRepository(SQLAlchemyRepository):
    model = Market
