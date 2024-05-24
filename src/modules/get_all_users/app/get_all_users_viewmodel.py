from typing import List

from src.shared.domain.entities.user import User


class UserViewmodel:
    def __init__(self, user: User):
        self.account = user.account
        self.agency = user.agency
        self.name = user.name
        self.current_balance = user.current_balance

    def to_dict(self):
        return {
            'current_balance': self.current_balance,
            'name': self.name,
            'agency': self.agency,
            'account': self.account
        }


class GetAllUsersViewmodel:
    def __init__(self, users_list: List[User]):
        self.users_viewmodel_list = [UserViewmodel(user) for user in users_list]

    def to_dict(self):
        return {
            "all_users": [viewmodel.to_dict() for viewmodel in self.users_viewmodel_list],
            "message": "all users has been retrieved"
        }
