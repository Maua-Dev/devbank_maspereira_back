from typing import List

from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


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

    def get_user(self, user_id: int) -> User:
        for user in self.users:
            if user.current_balance == user_id:
                return user
        raise NoItemsFound("user_id")

    def get_all_user(self) -> List[User]:
        return self.users

    def create_user(self, new_user: User) -> User:
        self.users.append(new_user)
        self.user_counter += 1
        return new_user

    def delete_user(self, user_id: int) -> User:
        for idx, user in enumerate(self.users):
            if user.current_balance == user_id:
                return self.users.pop(idx)

        raise NoItemsFound("user_id")

    def update_user(self, user_id: int, new_name: str) -> User:
        for user in self.users:
            if user.current_balance == user_id:
                user.name = new_name
                return user

        raise NoItemsFound("user_id")

    def get_user_counter(self) -> int:
        return self.user_counter
