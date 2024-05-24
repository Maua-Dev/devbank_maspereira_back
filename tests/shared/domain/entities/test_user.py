from src.shared.domain.entities.user import User
from src.shared.helpers.errors.domain_errors import EntityError
import pytest


class Test_User:
    def test_user(self):
        User(name="VITOR", agency="0000", current_balance=1.0, account="12345-6")

    def test_user_name_is_none(self):
        with pytest.raises(EntityError):
            User(name=None, agency="0000", current_balance=1.0, account="12345-6")

    def test_user_name_has_wrong_chars(self):
        with pytest.raises(EntityError):
            User(name="*123", agency="0000", current_balance=1.0, account="12345-6")

    def test_user_name_is_not_str(self):
        with pytest.raises(EntityError):
            User(name=1, agency="0000", current_balance=1.0, account="12345-6")

    def test_user_name_is_shorter_than_min_length(self):
        with pytest.raises(EntityError):
            User(name="V", agency="0000", current_balance=1.0, account="12345-6")

    def test_user_agency_is_none(self):
        with pytest.raises(EntityError):
            User(name="VITOR", agency=None, current_balance=1.0, account="12345-6")

    def test_user_agency_is_not_str(self):
        with pytest.raises(EntityError):
            User(name="VITOR", agency=0000, current_balance=1.0, account="12345-6")

    def test_user_agency_is_different_from_4_chars(self):
        with pytest.raises(EntityError):
            User(name="VITOR", agency="00000", current_balance=1.0, account="12345-6")

    def test_user_agency_has_wrong_chars(self):
        with pytest.raises(EntityError):
            User(name="VITOR", agency="000a", current_balance=1.0, account="12345-6")

    def test_user_current_balance_is_not_float(self):
        with pytest.raises(EntityError):
            User(name="VITOR", agency="0000", current_balance="1,0", account="12345-6")

    def test_user_current_balance_is_negative(self):
        with pytest.raises(EntityError):
            User(name="VITOR", agency="0000", current_balance=-1.0, account="12345-6")

    def test_user_account_is_none(self):
        with pytest.raises(EntityError):
            User(name="VITOR", agency="0000", current_balance=1.0, account=None)

    def test_user_account_is_not_str(self):
        with pytest.raises(EntityError):
            User(name="VITOR", agency="0000", current_balance=1.0, account=1)

    def test_user_account_is_different_from_7_chars(self):
        with pytest.raises(EntityError):
            User(name="VITOR", agency="0000", current_balance=1.0, account="123456")

    def test_user_account_has_wrong_chars(self):
        with pytest.raises(EntityError):
            User(name="VITOR", agency="0000", current_balance=1.0, account="1234s-6")
