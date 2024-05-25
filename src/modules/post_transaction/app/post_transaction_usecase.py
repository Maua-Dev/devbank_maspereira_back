from src.shared.domain.entities.transaction import Transaction
from typing import List, Dict
from src.shared.domain.repositories.transaction_repository.transactions_repository_interface import ITransactionsRepository


class PostTransactionUsecase:
    def __init__(self, repo: ITransactionsRepository):
        self.repo = repo

    def __call__(self) -> list[Transaction]:
        all_history_list = self.repo.get_transactions_history()

        return all_history_list
