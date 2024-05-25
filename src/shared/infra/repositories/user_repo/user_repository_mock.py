from typing import List

from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository.user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    users: List[User]
    user_counter: int

    def __init__(self):
        self.users = [
            User(name="Bruno Soller", agency="0000", current_balance=1.0, account="12345-6"),
            User(name="Vitor Brancas", agency="0000", current_balance=2.0, account="65432-1"),
            User(name="João Vilas", agency="0000", current_balance=3.0, account="32456-7")
        ]
        self.user_counter = 3

    def get_all_user(self) -> List[User]:
        return self.users

    def update_current_balance(self, current_balance: float = None) -> list[User]:
        self.users.current_balance = current_balance
        return self.users
