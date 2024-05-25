from .post_transaction_controller import PostTransactionController
from .post_transaction_usecase import PostTransactionUsecase
from src.shared.domain.repositories.transaction_repository.transactions_repository_interface import ITransactionsRepository
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo: ITransactionsRepository = Environments.get_history_repo()()
usecase = PostTransactionUsecase(repo)
controller = PostTransactionController(usecase)


def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
