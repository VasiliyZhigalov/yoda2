from unittest import TestCase

from src.api.sber_market_api import SberMarketApi


class TestSberMarketApi(TestCase):
    def test_get_products(self):
        smapi = SberMarketApi()
        prods = smapi.get_products("бананы","lenta",4)
        print(prods)