import abc

from src.shared.helpers.errors.domain_errors import EntityError


class Transaction(abc.ABC):
    transaction_type: str
    value: int
    current_balance: float
    timestamp: int

    def __init__(self, transaction_type: str, value: int, current_balance: float, timestamp: int):
        if not Transaction.validate_name(transaction_type):
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
    def validate_name(name: str) -> bool:
        if name is None:
            return False
        elif type(name) is not str:
            return False
        elif len(name) < 2:
            return False
        return True

    @staticmethod
    def validate_value(value: int) -> bool:
        if value is None:
            return False
        elif type(value) is not int:
            return False
        return True

    @staticmethod
    def validate_current_balance(current_balance: float) -> bool:
        if current_balance is None:
            return False
        elif type(current_balance) is not float:
            return False
        elif current_balance < 0.0:
            return False
        return True

    @staticmethod
    def validate_timestamp(timestamp: float) -> bool:
        if timestamp is None:
            return False
        elif type(timestamp) is not float:
            return False
        elif timestamp < 0.0:
            return False
        return True

    def __repr__(self):
        return f"User(transaction_type={self.transaction_type}, value={self.value}, current_balance={self.current_balance}, timestamp={self.timestamp})"
