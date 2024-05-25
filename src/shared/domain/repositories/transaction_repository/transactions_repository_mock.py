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
        self.transaction = Transaction(
            transaction_type=TransactionEnum.DEPOSIT.value,
            current_balance=1000.0,
            timestamp=32131,
            value=200
        )

    def post_transaction(self, transaction: Transaction = None) -> Dict[str, float]:
        if transaction.transaction_type == TransactionEnum.DEPOSIT:
            self.transaction.current_balance = transaction.current_balance + transaction.value
        elif transaction.transaction_type == TransactionEnum.WITHDRAW:
            self.transaction.current_balance = transaction.current_balance - transaction.value

        self.history.all_transactions.append(transaction)
        return {"current_balance": transaction.current_balance, "timestamp": transaction.timestamp}

    def get_transactions_history(self) -> History:
        return self.history
