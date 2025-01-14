from typing import List

from src.shared.domain.entities.transaction import Transaction


class PostTransactionViewmodel:
    def __init__(self, transaction: Transaction):
        self.transaction_type = transaction.transaction_type
        self.value = transaction.value
        self.timestamp = transaction.timestamp
        self.current_balance = transaction.current_balance

    def to_dict(self):
        return {
            'current_balance': self.current_balance,
            'timestamp': self.timestamp
        }


class HistoryTransactionViewmodel:
    def __init__(self, transactions_list: List[Transaction]):
        self.transactions_viewmodel_list = [PostTransactionViewmodel(transaction) for transaction in transactions_list]

    def to_dict(self):
        return {
            "all_transactions": [viewmodel.to_dict() for viewmodel in self.transactions_viewmodel_list],
            "message": "all transactions has been retrieved"
        }
