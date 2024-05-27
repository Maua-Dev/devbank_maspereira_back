from src.modules.post_transaction.app.post_transaction_usecase import PostTransactionUsecase
from src.shared.infra.repositories.transaction_repo.transaction_repository_mock import TransactionRepositoryMock


class Test_GetAllUsersUsecase:

    def test_get_all_users_usecase(self):
        repo_mock = TransactionRepositoryMock()
        usecase = PostTransactionUsecase(repo_mock)

        all_users_list_returned = usecase()

        assert all_users_list_returned == repo_mock.transactions
        assert len(all_users_list_returned) == len(repo_mock.transactions)

