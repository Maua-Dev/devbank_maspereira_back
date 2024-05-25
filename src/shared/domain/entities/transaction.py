import abc

from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.enums.transaction_enum import TransactionEnum


class Transaction(abc.ABC):
    transaction_type: str
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, transaction_type: str, value: float, current_balance: float, timestamp: float):
        if not Transaction.validate_transaction_type(transaction_type):
            raise EntityError("transaction_type")
        self.name = transaction_type

        if not Transaction.validate_value(value):
            raise EntityError("value")
        self.agency = value

        if not Transaction.validate_current_balance(current_balance):
            raise EntityError("current_balance")
        self.account = current_balance

        if not Transaction.validate_timestamp(timestamp):
            raise EntityError("timestamp")
        self.current_balance = timestamp

    @staticmethod
    def validate_transaction_type(transaction_type: str) -> bool:
        if transaction_type is None:
            return False
        elif transaction_type.lower() != TransactionEnum.DEPOSIT.value.lower().replace(" ", "") and transaction_type.lower() != TransactionEnum.WITHDRAW.value.lower().replace(" ", ""):  # nessa linha a gente verifica se o tipo da transação é deposit ou withdraw, com base no valor do TransactionEnum.DEPOSIT ou TransactionEnum.WITHDRAW
            return False
        return True

    @staticmethod
    def validate_value(value: float) -> bool:
        if value is None:
            return False
        try:
            value = float(value)
        except (ValueError, TypeError):
            return False
        if type(value) is not float:
            return False
        elif value < 0.0:
            return False
        return True

    @staticmethod
    def validate_current_balance(current_balance: float) -> bool:
        if current_balance is None:
            return False
        try:
            current_balance = float(current_balance)
        except (ValueError, TypeError):
            return False
        if type(current_balance) is not float:
            return False
        elif current_balance < 0.0:
            return False
        return True

    @staticmethod
    def validate_timestamp(timestamp: float) -> bool:
        if timestamp is None:
            return False
        try:
            timestamp = float(timestamp)
        except (ValueError, TypeError):
            return False
        if type(timestamp) is not float:
            return False
        elif timestamp < 0.0:
            return False
        return True

    def __repr__(self):
        return f"Transaction(transaction_type={self.transaction_type}, value={self.value}, current_balance={self.current_balance}, timestamp={self.timestamp})"
