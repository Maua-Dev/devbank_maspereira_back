from src.shared.domain.entities.transaction import Transaction
from src.shared.infra.dto.transaction_dynamo_dto import TransactionDynamoDTO
from src.shared.infra.repositories.transaction_repo.transaction_repository_mock import TransactionRepositoryMock


class Test_TransactionDynamoDto:
    def test_from_entity(self):
        repo = TransactionRepositoryMock()

        transaction_dto = TransactionDynamoDTO.from_entity(transaction=repo.transactions[0])

        expected_selfie_dto = TransactionDynamoDTO(
            transaction_type=repo.transactions[0].transaction_type,
            timestamp=repo.transactions[0].timestamp,
            current_balance=repo.transactions[0].current_balance,
            value=repo.transactions[0].value
        )

        assert transaction_dto == expected_selfie_dto

    def test_to_dynamo(self):
        repo = TransactionRepositoryMock()

        transaction_dto = TransactionDynamoDTO(
            transaction_type=repo.transactions[0].transaction_type,
            timestamp=repo.transactions[0].timestamp,
            current_balance=repo.transactions[0].current_balance,
            value=repo.transactions[0].value
        )

        transaction_dynamo = transaction_dto.to_dynamo()

        expected_dict = {
            "entity": "transaction",
            "transaction_type": repo.transactions[0].transaction_type,
            "timestamp": repo.transactions[0].timestamp,
            "current_balance": repo.transactions[0].current_balance,
            "value": repo.transactions[0].value
        }

        assert transaction_dto.to_dynamo() == expected_dict

    def test_from_dynamo(self):
        dynamo_dict = {'Item': {'current_balance': 1000,
                                'transaction_type': 'deposit',
                                'SK': '#1',
                                'timestamp': '32131',
                                'PK': 'user#1',
                                'entity': 'transaction',
                                'value': '200'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        transaction_dto = TransactionDynamoDTO.from_dynamo(transaction_data=dynamo_dict["Item"])

        expected_user_dto = TransactionDynamoDTO(
            transaction_type="deposit",
            current_balance=1000.0,
            timestamp=32131,
            value=200
        )

        assert transaction_dto == expected_user_dto

    def test_to_entity(self):
        repo = TransactionRepositoryMock()

        transaction_dto = TransactionDynamoDTO(
            transaction_type=repo.transactions[0].transaction_type,
            timestamp=repo.transactions[0].timestamp,
            current_balance=repo.transactions[0].current_balance,
            value=repo.transactions[0].value
        )

        transaction = transaction_dto.to_entity()

        assert transaction.transaction_type == repo.transactions[0].transaction_type
        assert transaction.timestamp == repo.transactions[0].timestamp
        assert transaction.current_balance == repo.transactions[0].current_balance
        assert transaction.value == repo.transactions[0].value

    def test_from_dynamo_to_entity(self):
        dynamo_item = {'Item': {'current_balance': 1000,
                                'transaction_type': 'deposit',
                                'SK': '#1',
                                'timestamp': '32131',
                                'PK': 'user#1',
                                'entity': 'transaction',
                                'value': '200'}}

        transaction_dto = TransactionDynamoDTO.from_dynamo(transaction_data=dynamo_item["Item"])

        transaction = transaction_dto.to_entity()

        expected_transaction = Transaction(
            transaction_type="deposit",
            current_balance=1000.0,
            timestamp=32131,
            value=200
        )

        assert transaction.transaction_type == expected_transaction.transaction_type
        assert transaction.timestamp == expected_transaction.timestamp
        assert transaction.current_balance == expected_transaction.current_balance
        assert transaction.value == expected_transaction.value

    def test_from_entity_to_dynamo(self):
        repo = TransactionRepositoryMock()

        transaction_dto = TransactionDynamoDTO.from_entity(transaction=repo.transactions[0])

        transaction_dynamo = transaction_dto.to_dynamo()

        expected_dict = {
            "entity": "transaction",
            "transaction_type": repo.transactions[0].transaction_type,
            "timestamp": repo.transactions[0].timestamp,
            "current_balance": repo.transactions[0].current_balance,
            "value": repo.transactions[0].value
        }

        assert transaction_dynamo == expected_dict
