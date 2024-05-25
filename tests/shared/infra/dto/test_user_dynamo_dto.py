from src.shared.domain.entities.user import User
from src.shared.infra.dto.user_dynamo_dto import UserDynamoDTO
from src.shared.infra.repositories.user_repo.user_repository_mock import UserRepositoryMock


class Test_UserDynamoDto:
    def test_from_entity(self):
        repo = UserRepositoryMock()

        user_dto = UserDynamoDTO.from_entity(user=repo.users[0])

        expected_selfie_dto = UserDynamoDTO(
            name=repo.users[0].name,
            agency=repo.users[0].agency,
            current_balance=repo.users[0].current_balance,
            account=repo.users[0].account
        )

        assert user_dto == expected_selfie_dto

    def test_to_dynamo(self):
        repo = UserRepositoryMock()

        user_dto = UserDynamoDTO(
            name=repo.users[0].name,
            agency=repo.users[0].agency,
            current_balance=repo.users[0].current_balance,
            account=repo.users[0].account
        )

        user_dynamo = user_dto.to_dynamo()

        expected_dict = {
            "entity": "user",
            "name": repo.users[0].name,
            "agency": repo.users[0].agency,
            "current_balance": repo.users[0].current_balance,
            "account": repo.users[0].account
        }

        assert user_dto.to_dynamo() == expected_dict

    def test_from_dynamo(self):
        dynamo_dict = {'Item': {'current_balance': 1.0,
                                'name': 'Bruno Soller',
                                'SK': '#1',
                                'account': '0000',
                                'PK': 'user#1',
                                'entity': 'user',
                                'agency': '12345-6'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        user_dto = UserDynamoDTO.from_dynamo(user_data=dynamo_dict["Item"])

        expected_user_dto = UserDynamoDTO(
            name="Bruno Soller",
            agency='12345-6',
            current_balance=1.0,
            account="0000"
        )

        assert user_dto == expected_user_dto

    def test_to_entity(self):
        repo = UserRepositoryMock()

        user_dto = UserDynamoDTO(
            name=repo.users[0].name,
            agency=repo.users[0].agency,
            current_balance=repo.users[0].current_balance,
            account=repo.users[0].account
        )

        user = user_dto.to_entity()

        assert user.name == repo.users[0].name
        assert user.agency == repo.users[0].agency
        assert user.current_balance == repo.users[0].current_balance
        assert user.account == repo.users[0].account

    def test_from_dynamo_to_entity(self):
        dynamo_item = {'Item': {'current_balance': 1.0,
                                'name': 'Bruno Soller',
                                'SK': '#1',
                                'account': '12345-6',
                                'PK': 'user#1',
                                'entity': 'user',
                                'agency': '0000'}}

        user_dto = UserDynamoDTO.from_dynamo(user_data=dynamo_item["Item"])

        user = user_dto.to_entity()

        expected_user = User(
            name="Bruno Soller",
            agency="0000",
            current_balance=1.0,
            account="12345-6"
        )

        assert user.name == expected_user.name
        assert user.agency == expected_user.agency
        assert user.current_balance == expected_user.current_balance
        assert user.account == expected_user.account

    def test_from_entity_to_dynamo(self):
        repo = UserRepositoryMock()

        user_dto = UserDynamoDTO.from_entity(user=repo.users[0])

        user_dynamo = user_dto.to_dynamo()

        expected_dict = {
            "entity": "user",
            "name": repo.users[0].name,
            "agency": repo.users[0].agency,
            "current_balance": repo.users[0].current_balance,
            "account": repo.users[0].account
        }

        assert user_dynamo == expected_dict
