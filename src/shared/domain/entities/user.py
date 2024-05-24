import abc
import re

from src.shared.helpers.errors.domain_errors import EntityError


class User(abc.ABC):
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(self, name: str, agency: str, account: str, current_balance: float):
        if not User.validate_name(name):
            raise EntityError("name")
        self.name = name

        if not User.validate_agency(agency):
            raise EntityError("agency")
        self.agency = agency

        if not User.validate_account(account):
            raise EntityError("account")
        self.account = account

        if not User.validate_current_balance(current_balance):
            raise EntityError("current_balance")
        self.current_balance = current_balance

    @staticmethod
    def validate_name(name: str) -> bool:
        if name is None:
            return False
        elif type(name) is not str:
            return False
        elif len(name) < 2:
            return False
        regex = re.compile(r"^[a-zA-ZÀ-ÿ\s]+$")
        return bool(re.fullmatch(regex, name))

    @staticmethod
    def validate_agency(agency: str) -> bool:
        if agency is None:
            return False
        elif type(agency) is not str:
            return False
        elif len(agency) != 4:
            return False
        regex = re.compile(r"^\d{4}$")  # função que verifica se o texto é composto somente de números
        return bool(re.fullmatch(regex, agency))

    @staticmethod
    def validate_account(account: str) -> bool:
        if account is None:
            return False
        elif type(account) is not str:
            return False
        elif len(account) != 7:  # account tem que ser do tipo xxxxx-x
            return False
        regex = re.compile(r"^\d{5}-\d$")
        return bool(re.fullmatch(regex, account))

    @staticmethod
    def validate_current_balance(current_balance: float) -> bool:
        if current_balance is None:
            return False
        try:
            current_balance = float(current_balance)
        except (ValueError, TypeError):
            return False
        if type(current_balance) is not float:
            return False
        elif current_balance < 0.0:
            return False
        return True

    def __repr__(self):
        return f"User(name={self.name}, agency={self.agency}, account={self.account}, current_balance={self.current_balance})"
