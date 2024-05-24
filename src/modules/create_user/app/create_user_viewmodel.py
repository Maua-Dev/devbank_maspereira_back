from src.shared.domain.entities.user import User
from src.shared.domain.enums.state_enum import STATE


class CreateUserViewmodel:
    user_id: int
    name: str
    email: str
    state: STATE

    def __init__(self, user: User):
        self.user_id = user.current_balance
        self.name = user.name
        self.email = user.agency
        self.state = user.state

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'state': self.state.value,
            'message': "the user was created successfully"
        }
