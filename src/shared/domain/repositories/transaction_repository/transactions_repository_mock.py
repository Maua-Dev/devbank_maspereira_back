from typing import Dict
from ...entities.history import History
from ...entities.transaction import Transaction
from ...enums.transaction_enum import TransactionEnum

from .transactions_repository_interface import ITransactionsRepository


class TransactionsRepositoryMock(ITransactionsRepository):
    history: History
    transaction: Transaction

    def __init__(self):
        self.history = History()

    def create_transaction(self, transaction: Transaction = None) -> Dict[str, float]:
        if transaction.transaction_type == TransactionEnum.DEPOSIT:
            transaction.current_balance = transaction.current_balance + transaction.value
        elif transaction.transaction_type == TransactionEnum.WITHDRAW:
            transaction.current_balance = transaction.current_balance - transaction.value

        transaction = Transaction(
            transaction_type=transaction.transaction_type,
            value=transaction.value,
            current_balance=transaction.current_balance,
            timestamp=transaction.timestamp
        )

        self.history.all_transactions.append(transaction)
        return {"current_balance": transaction.current_balance, "timestamp": transaction.timestamp}

    def get_transactions_history(self):
        return self.history
