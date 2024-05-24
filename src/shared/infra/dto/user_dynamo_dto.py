from decimal import Decimal

from src.shared.domain.entities.user import User
from src.shared.domain.enums.state_enum import STATE


class UserDynamoDTO:
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(self, name: str, agency: str, account: str, current_balance: float):
        self.name = name
        self.agency = agency
        self.current_balance = current_balance
        self.account = account

    @staticmethod
    def from_entity(user: User) -> "UserDynamoDTO":
        """
        Parse data from User to UserDynamoDTO
        """
        return UserDynamoDTO(
            name=user.name,
            agency=user.agency,
            current_balance=user.current_balance,
            account=user.account
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from UserDynamoDTO to dict
        """
        return {
            "entity": "user",
            "name": self.name,
            "agency": self.agency,
            "current_balance": self.current_balance,
            "account": self.account
        }

    @staticmethod
    def from_dynamo(user_data: dict) -> "UserDynamoDTO":
        """
        Parse data from DynamoDB to UserDynamoDTO
        @param user_data: dict from DynamoDB
        """
        return UserDynamoDTO(
            name=user_data["name"],
            agency=user_data["agency"],
            current_balance=float(user_data["current_balance"]),
            account=user_data["account"]
        )

    def to_entity(self) -> User:
        """
        Parse data from UserDynamoDTO to User
        """
        return User(
            name=self.name,
            agency=self.agency,
            current_balance=self.current_balance,
            account=self.account
        )

    def __repr__(self):
        return f"UserDynamoDto(name={self.name}, agency={self.agency}, current_balance={self.current_balance}, account={self.account})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
