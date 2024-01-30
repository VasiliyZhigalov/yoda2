from typing import List

from src.api.market_api import AbstractMarketApi
from src.api.sber_market_api import SberMarketApi
from src.models.model import UserQuery
from src.repositories.market import MarketRepository
from src.repositories.product import ProductRepository
from src.repositories.repository import AbstractRepository
from src.repositories.user_query import UserQueryRepository
from src.schemas.product import ProductSchema
from src.schemas.user_query import UserQuerySchemaAdd, UserQuerySchema
from src.utils.user_query_utils import parse_user_query


class ShoppingListService:
    def __init__(self):
        self.apis: List[AbstractMarketApi] = [SberMarketApi(), ]
        self.query_repo: AbstractRepository = UserQueryRepository()
        self.market_repo: AbstractRepository = MarketRepository()
        self.product_repo: AbstractRepository = ProductRepository()

    def save_user_queries(self, user_queries_str: str, user_id: int) -> List[UserQuerySchema]:
        queries = parse_user_query(user_queries_str)
        for q in queries:
            q.user_id = user_id
            self.query_repo.add_one(q.model_dump())
        return self.query_repo.find_all_by_filter(user_id=user_id)

    def _get_query_list(self, user_id: int) -> List[UserQuerySchema]:
        return self.query_repo.find_all_by_filter(user_id=user_id)

    def get_products_by_user_queries(self, user_id: int) -> List[ProductSchema]:
        user_queries = self._get_query_list(user_id)
        markets = ['lenta', 'metro']
        for q in user_queries:
            query_id = q.id
            for api in self.apis:
                for m in markets:
                    market_id = self.market_repo.find_one(name=m).id
                    prods = api.get_products(query=q.product, market_name=m, max_count=3)
                    for p in prods:
                        print(p.title)
                        p.user_query_id = query_id
                        p.market_id = market_id
                        self.product_repo.add_one(p.model_dump())


if __name__ == "__main__":
    sl = ShoppingListService()
    query = UserQuerySchemaAdd(
        product='Кокос',
        quantity=1,
        unit='кг',
        user_id=1
    )
    sl.get_products_by_user_queries([query])
