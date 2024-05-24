from src.shared.domain.entities.user import User
from src.shared.helpers.errors.domain_errors import EntityError
import pytest


class Test_User:
    def test_user(self):
        User(name="VITOR", agency="0000", current_balance=1.0, account="12345-6")

    def test_user_name_is_none(self):
        with pytest.raises(EntityError):
            User(name=None, agency="0000", current_balance=1.0, account="12345-6")

    def test_user_name_is_not_str(self):
        with pytest.raises(EntityError):
            User(name=1, agency="0000", current_balance=1.0, account="12345-6")

    def test_user_name_is_shorter_than_min_length(self):
        with pytest.raises(EntityError):
            User(name="V", agency="0000", current_balance=1.0, account="12345-6")

    def test_user_agency_is_none(self):
        with pytest.raises(EntityError):
            User(name="VITOR", agency=None, current_balance=1.0, account="12345-6")

    def test_user_agency_is_not_valid(self):
        with pytest.raises(EntityError):
            User(name="VITOR", agency="000", current_balance=1.0, account="12345-6")

    def test_user_current_balance_is_not_int(self):
        with pytest.raises(EntityError):
            User(name="VITOR", agency="0000", current_balance="1", account="12345-6")

    def test_user_current_balance_is_negative(self):
        with pytest.raises(EntityError):
            User(name="VITOR", agency="0000", current_balance=-1.0, account="12345-6")

    # TODO: Fazer testes para account
