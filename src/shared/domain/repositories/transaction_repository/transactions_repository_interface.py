from abc import ABC, abstractmethod
from typing import List, Dict

from ...entities.transaction import Transaction


class ITransactionsRepository(ABC):

    @abstractmethod
    def get_transactions_history(self) -> Dict[str, List[Transaction]]:
        """
        Returns all transactions in the database
        """
        pass

    @abstractmethod
    def create_transaction(self, transaction: Transaction = None) -> Transaction:
        """
        Create transaction in the database
        """
        pass
