from src.shared.domain.entities.transaction import Transaction
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.transaction_repo.transaction_repository_mock import TransactionRepositoryMock
import pytest


class Test_UserRepositoryMock:
    def test_get_transactions_history(self):
        repo = TransactionRepositoryMock()
        history = repo.get_transactions_history()

        assert history["all_transactions"]
        # TODO: terminar esse arquivo todo

    def test_post_transaction(self):
        repo = TransactionRepositoryMock()
        transactions = repo.post_transaction()
        assert transactions.current_balance != 1000
