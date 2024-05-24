from src.modules.get_all_users.app.get_all_users_viewmodel import GetAllUsersViewmodel, UserViewmodel
from src.shared.domain.entities.user import User


class Test_GetAllUsersViewmodel:
    all_users_list = [
        User(current_balance=1.0,
             name="Lucas Duez",
             agency="0000",
             account="12345-6"),

        User(current_balance=2.0,
             name="Laura Blablachan",
             agency="0000",
             account="12345-6")
    ]

    def test_get_all_users_viewmodel(self):
        viewmodel = GetAllUsersViewmodel(self.all_users_list)

        expected = {
            "all_users": [
                {
                    'current_balance': 1.0,
                    'name': "Lucas Duez",
                    'agency': "0000",
                    'account': '12345-6'
                },
                {
                    'current_balance': 2.0,
                    'name': "Laura Blablachan",
                    'agency': "0000",
                    'account': '12345-6'
                }
            ],
            "message": "all users has been retrieved"
        }

        response = viewmodel.to_dict()

        assert response == expected

    def test_user_viewmodel(self):
        viewmodel = UserViewmodel(
            User(current_balance=2.0,
                 name="Laura Blablachan",
                 agency="0000",
                 account="12345-6")
        )

        response = viewmodel.to_dict()

        expected = {
                    'current_balance': 2.0,
                    'name': "Laura Blablachan",
                    'agency': "0000",
                    'account': '12345-6'
        }

        assert response == expected
