from unittest import TestCase
from src.repositories.user import UserRepository
from src.schemas.user import UserSchemaAdd


class TestUserRepository(TestCase):

    def test_add_user(self):
        user_repo = UserRepository()
        user = UserSchemaAdd(
            user_id=3,
            name='Вася',
            role='админ',
            latitude='123',
            longitude='345'
        )
        user_dict = user.model_dump()
        user_id = user_repo.add_one(user_dict)
        print(user_id)

    def test_find_all(self):
        user_repo = UserRepository()
        users = user_repo.find_all()
        print(users)

    def test_find_one(self):
        user_repo = UserRepository()
        user = user_repo.find_one(name='Vasiliy_Zhigalov')
        print(user)

    def test_edit_one(self):
        user_repo = UserRepository()
        user_id = user_repo.edit_one(id=1, data={'latitude': '213'})
        print(user_id)

    def test_del_one(self):
        user_repo = UserRepository()
        user_repo.delete_one(id = 24)
