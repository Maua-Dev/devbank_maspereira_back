from abc import ABC, abstractmethod
from typing import List, Dict

from ...entities.transaction import Transaction
from ...entities.user import User


class ITransactionsRepository(ABC):

    @abstractmethod
    def get_transactions_history(self) -> Dict[str, List[Transaction]]:
        """
        Returns all transactions in the database
        """
        pass

    @abstractmethod
    def post_transaction(self, transaction: Transaction = None) -> Transaction:
        """
        Create transaction in the database
        """
        pass
