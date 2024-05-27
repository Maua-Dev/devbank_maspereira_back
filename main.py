from fastapi import FastAPI
from typing import Dict, Any
from src.modules.get_all_users.app.get_all_users_presenter import lambda_handler as get_all_users
from src.modules.post_transaction.app.post_transaction_presenter import lambda_handler as post_tr
from pydantic import BaseModel

api = FastAPI()


class Transaction(BaseModel):
    transaction_type: str
    value: float
    current_balance: float
    timestamp: float


class History(BaseModel):
    all_transactions: Dict[str, Transaction]


class Event:
    headers: Dict[str, Any]
    body: Dict[str, Any]
    queryStringParameters: Dict[str, Any]

    def __init__(self, headers=None, body=None, queryStringParameters=None):
        self.headers = headers or {}
        self.body = body or {}
        self.queryStringParameters = queryStringParameters or {}

    def to_dict(self):
        return {
            "headers": self.headers,
            "body": self.body,
            "queryStringParameters": self.queryStringParameters
        }


@api.get("/")
def get_all_user():
    event = Event().to_dict()
    return get_all_users(event=event, context=None)


@api.get("/history")
def get_history():
    event = Event().to_dict()
    return post_tr(event=event, context=None)


@api.post("/transaction")
def post_transaction():
    event = Event().to_dict()
    return post_tr(event=event, context=None)
