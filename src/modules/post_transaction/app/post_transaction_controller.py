from src.shared.helpers.external_interfaces.external_interface import IRequest
from .post_transaction_usecase import PostTransactionUsecase
from .post_transaction_viewmodel import PostTransactionViewmodel
from src.shared.domain.entities.transaction import Transaction
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import NotFound, OK, BadRequest, InternalServerError


class PostTransactionController:
    def __init__(self, usecase: PostTransactionUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest):
        try:
            all_transactions_list: list[Transaction] = self.usecase()

            viewmodel = PostTransactionViewmodel(all_transactions_list[0])

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:

            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except WrongTypeParameter as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])
