from typing import List, Dict

from src.shared.domain.entities.transaction import Transaction
from src.shared.domain.repositories.transaction_repository.transactions_repository_interface import \
    ITransactionsRepository


class TransactionRepositoryMock(ITransactionsRepository):
    transactions: List[Transaction]
    transaction_counter: int

    def __init__(self):
        self.transactions = [
            Transaction(transaction_type="deposit", timestamp=123456, value=200,
                        current_balance=1000),
            Transaction(transaction_type="withdraw", timestamp=654321, value=200,
                        current_balance=1000)
        ]
        self.transaction_counter = 2
        self.new_value = 0

    def get_transactions_history(self) -> Dict[str, List[Transaction]]:
        return {
            "all_transactions": self.transactions
        }

    def post_transaction(self, transaction: Transaction = None) -> Transaction:
        if transaction.transaction_type.lower() == "deposit":
            self.new_value = transaction.current_balance + transaction.value
        elif transaction.transaction_type.lower() == "withdraw":
            self.new_value = transaction.current_balance - transaction.value
        return Transaction(transaction_type=transaction.transaction_type, value=transaction.value, timestamp=transaction.timestamp, current_balance=self.new_value)
