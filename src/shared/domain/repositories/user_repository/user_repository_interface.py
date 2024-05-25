from abc import ABC, abstractmethod
from typing import List

from src.shared.domain.entities.user import User


class IUserRepository(ABC):
    @abstractmethod
    def get_all_user(self) -> List[User]:
        """
        Returns user in the database
        """
        pass

    @abstractmethod
    def update_current_balance(self, current_balance: float = None) -> User:
        """
        Updates the item with the given id.
        If the item does not exist, returns None
        """
        pass
