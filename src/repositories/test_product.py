from unittest import TestCase

from src.repositories.product import ProductRepository
from src.schemas.product import ProductSchemaAdd


class TestProductRepository(TestCase):


    def test_add_product(self):
        new_product = ProductSchemaAdd(
            title="Мясо курицы",
            price=3.5,
            image="ссылка на картинку",
            href="ссылка"
        )
        self.prod_repo = ProductRepository()
        prod_dict = new_product.model_dump()
        prod_id = self.prod_repo.add_one(prod_dict)
        print(prod_id)

    def test_find_all(self):
        self.prod_repo = ProductRepository()
        prod_repo = ProductRepository()
        prods = prod_repo.find_all()
        print(prods)

    def test_find_one(self):
        self.prod_repo = ProductRepository()
        user = self.prod_repo.find_one(title='Мясо курицы')
        print(user)

    def test_edit_one(self):
        self.prod_repo = ProductRepository()
        user_id = self.prod_repo.edit_one(id=1, data={'title': 'Кролик'})
        print(user_id)

    def test_del_one(self):
        self.prod_repo = ProductRepository()
        self.prod_repo.delete_one(id=1)
