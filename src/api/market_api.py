from abc import ABC, abstractmethod
from typing import List

from src.schemas.product import ProductSchemaAdd


class AbstractMarketApi(ABC):

    @abstractmethod
    def get_products(self, query: str, market_name: str, max_count: int) -> List[ProductSchemaAdd]:
        raise NotImplementedError
