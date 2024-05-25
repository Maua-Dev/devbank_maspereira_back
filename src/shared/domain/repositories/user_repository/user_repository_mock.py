from ...entities.user import User
from .user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    user: User

    def __init__(self):
        self.user = User(name="Vitor Soller", agency="0000", account="00000-0", current_balance=1000.0)

    def get_all_user(self) -> User:
        return self.user

    def update_current_balance(self, current_balance: float = None) -> User:
        self.user.current_balance = current_balance
        return self.user
