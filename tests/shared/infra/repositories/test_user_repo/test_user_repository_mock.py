from src.shared.domain.entities.user import User
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.user_repo.user_repository_mock import UserRepositoryMock
import pytest


class Test_UserRepositoryMock:
    def test_get_user(self):
        repo = UserRepositoryMock()
        user = repo.get_all_user()

        assert user[0].name == "Bruno Soller"
        assert user[0].agency == "0000"
        assert user[0].current_balance == 1.0
        assert user[0].account == "12345-6"

    def test_get_all_user(self):
        repo = UserRepositoryMock()
        users = repo.get_all_user()
        assert len(users) == 3
