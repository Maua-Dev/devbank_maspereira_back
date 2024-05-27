from src.shared.domain.entities.transaction import Transaction


class TransactionDynamoDTO:
    transaction_type: str
    value: float
    timestamp: float
    current_balance: float

    def __init__(self, transaction_type: str, value: float, timestamp: float, current_balance: float):
        self.transaction_type = transaction_type
        self.value = value
        self.timestamp = timestamp
        self.current_balance = current_balance

    @staticmethod
    def from_entity(transaction: Transaction) -> "TransactionDynamoDTO":
        """
        Parse data from Transaction to UserDynamoDTO
        """
        return TransactionDynamoDTO(
            transaction_type=transaction.transaction_type,
            value=transaction.value,
            current_balance=transaction.current_balance,
            timestamp=transaction.timestamp
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from UserDynamoDTO to dict
        """
        return {
            "entity": "transaction",
            "transaction_type": self.transaction_type,
            "value": self.value,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp
        }

    @staticmethod
    def from_dynamo(transaction_data: dict) -> "TransactionDynamoDTO":
        """
        Parse data from DynamoDB to TransactionDynamoDTO
        @param transaction_data: dict from DynamoDB
        """
        return TransactionDynamoDTO(
            transaction_type=transaction_data["transaction_type"],
            value=transaction_data["value"],
            current_balance=transaction_data["current_balance"],
            timestamp=transaction_data["timestamp"]
        )

    def to_entity(self) -> Transaction:
        """
        Parse data from TransactionDynamoDTO to Transaction
        """
        return Transaction(
            transaction_type=self.transaction_type,
            value=self.value,
            current_balance=self.current_balance,
            timestamp=self.timestamp
        )

    def __repr__(self):
        return f"TransactionDynamoDto(transaction_type={self.transaction_type}, value={self.value}, current_balance={self.current_balance}, timestamp={self.timestamp})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
