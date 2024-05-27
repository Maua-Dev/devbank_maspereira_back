from src.modules.post_transaction.app.post_transaction_controller import PostTransactionController
from src.modules.post_transaction.app.post_transaction_usecase import PostTransactionUsecase
from src.shared.infra.repositories.transaction_repo.transaction_repository_mock import TransactionRepositoryMock


class Test_PostTransactionController:

    def test_post_transaction_controller(self):
        repo_mock = TransactionRepositoryMock()
        post_transactions_usecase = PostTransactionUsecase(repo_mock)
        controller = PostTransactionController(post_transactions_usecase)

        response = controller(None)

        assert response.status_code == 200

