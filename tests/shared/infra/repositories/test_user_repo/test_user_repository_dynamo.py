import os

import pytest

from src.shared.infra.repositories.user_repo.user_repository_dynamo import UserRepositoryDynamo
from src.shared.infra.repositories.user_repo.user_repository_mock import UserRepositoryMock


class Test_UserRepositoryDynamo:
    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_all_user(self):
        os.environ["STAGE"] = "TEST"

        user_repository = UserRepositoryDynamo()
        user_repository_mock = UserRepositoryMock()
        resp = user_repository.get_all_user()

        assert len(user_repository_mock.users) == len(resp)
