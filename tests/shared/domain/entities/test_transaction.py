from src.shared.domain.entities.transaction import Transaction
from src.shared.helpers.errors.domain_errors import EntityError
import pytest


class Test_Transaction:
    def test_transaction(self):
        Transaction(transaction_type="deposit", value=200, current_balance=1000.0, timestamp=514564456)

    def test_transaction_transaction_type_is_none(self):
        with pytest.raises(EntityError):
            Transaction(transaction_type=None, value=200, current_balance=1000.0, timestamp=514564456)

    def test_transaction_transaction_type_is_not_deposit_or_withdraw(self):
        with pytest.raises(EntityError):
            Transaction(transaction_type="deposito", value=200, current_balance=1000.0, timestamp=514564456)

    def test_transaction_value_is_none(self):
        with pytest.raises(EntityError):
            Transaction(transaction_type="deposit", value=None, current_balance=1000.0, timestamp=514564456)

    def test_transaction_value_is_not_float(self):
        with pytest.raises(EntityError):
            Transaction(transaction_type="deposit", value="200,0", current_balance=1000.0, timestamp=514564456)

    def test_transaction_value_is_negative(self):
        with pytest.raises(EntityError):
            Transaction(transaction_type="deposit", value=-200, current_balance=1000.0, timestamp=514564456)

    def test_transaction_current_balance_is_none(self):
        with pytest.raises(EntityError):
            Transaction(transaction_type="deposit", value=200, current_balance=None, timestamp=514564456)

    def test_transaction_current_balance_is_not_float(self):
        with pytest.raises(EntityError):
            Transaction(transaction_type="deposit", value=200, current_balance="1000,0", timestamp=514564456)

    def test_transaction_current_balance_is_negative(self):
        with pytest.raises(EntityError):
            Transaction(transaction_type="deposit", value=200, current_balance=-1000.0, timestamp=514564456)

    def test_transaction_timestamp_is_none(self):
        with pytest.raises(EntityError):
            Transaction(transaction_type="deposit", value=200, current_balance=1000.0, timestamp=None)

    def test_transaction_timestamp_is_not_float(self):
        with pytest.raises(EntityError):
            Transaction(transaction_type="deposit", value=200, current_balance=1000.0, timestamp="string")

    def test_transaction_timestamp_is_negative(self):
        with pytest.raises(EntityError):
            Transaction(transaction_type="deposit", value=200, current_balance=1000.0, timestamp=-514564456)
