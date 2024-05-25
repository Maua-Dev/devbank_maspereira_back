from src.shared.domain.entities.transaction import Transaction
from src.shared.domain.repositories.transaction_repository.transactions_repository_interface import ITransactionsRepository
from src.shared.environments import Environments
from src.shared.infra.dto.transaction_dynamo_dto import TransactionDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class TransactionRepositoryDynamo(ITransactionsRepository):

    @staticmethod
    def partition_key_format(transaction_id) -> str:
        return f"user#{transaction_id}"

    @staticmethod
    def sort_key_format(transaction_id: int) -> str:
        return f"#{transaction_id}"

    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key,
                                       sort_key=Environments.get_envs().dynamo_sort_key)

    def get_transactions_history(self) -> list[Transaction]:
        resp = self.dynamo.get_all_items()
        transactions = []
        for item in resp['Items']:
            if item.get("entity") == 'transaction':
                transactions.append(TransactionDynamoDTO.from_dynamo(item).to_entity())

        return transactions

    def post_transaction(self, transaction: Transaction = None) -> Transaction:
        print(f"repo entered.\n Repo:{self}")
        print(self.dynamo.dynamo_table.__dict__)
        transaction.current_balance = transaction.current_balance + transaction.value
        print(f"nre user id: {transaction.current_balance}")
        transaction_dto = TransactionDynamoDTO.from_entity(transaction=transaction)
        resp = self.dynamo.put_item(partition_key=self.partition_key_format(transaction.current_balance),
                                    sort_key=self.sort_key_format(transaction_id=int(transaction.current_balance)),
                                    item=transaction_dto.to_dynamo(),
                                    is_decimal=True)
        return transaction
