from src.modules.post_transaction.app.post_transaction_viewmodel import PostTransactionViewmodel, HistoryTransactionViewmodel
from src.shared.domain.entities.transaction import Transaction


class Test_GetAllUsersViewmodel:
    all_transactions_list = [
        Transaction(transaction_type="deposit", timestamp=123456, value=200,
                    current_balance=1000),
        Transaction(transaction_type="withdraw", timestamp=654321, value=200,
                    current_balance=1000)
    ]

    def test_get_all_users_viewmodel(self):
        viewmodel = HistoryTransactionViewmodel(self.all_transactions_list)

        expected = {
            "all_transactions": [
                {
                    'transaction_type': "deposit",
                    'timestamp': 123456,
                    'value': 200,
                    'current_balance': 1000,
                },
                {
                    'transaction_type': "withdraw",
                    'timestamp': 654321,
                    'value': 200,
                    'current_balance': 1000,
                }
            ],
            "message": "all transactions has been retrieved"
        }

        response = viewmodel.to_dict()

        assert response == expected

    def test_user_viewmodel(self):
        viewmodel = PostTransactionViewmodel(
            Transaction(transaction_type="deposit", timestamp=123456, value=200,
                        current_balance=1000),
        )

        response = viewmodel.to_dict()

        expected = {
                    'transaction_type': "deposit",
                    'timestamp': 123456,
                    'value': 200,
                    'current_balance': 1000,
        }

        assert response == expected
