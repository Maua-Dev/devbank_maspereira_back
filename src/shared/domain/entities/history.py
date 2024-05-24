from typing import List
from .transaction import Transaction


class History:
    all_transactions: List[Transaction]

    def __init__(self, all_transactions: List[Transaction] = None):
        if all_transactions is None:
            all_transactions = []
        self.all_transactions = all_transactions

    def to_dict(self):
        return {
            "all_transactions": [transaction for transaction in self.all_transactions]
        }
