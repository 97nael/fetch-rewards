from pydantic import BaseModel
from datetime import datetime


class TransactionRequest(BaseModel):
    payer: str
    points: int
    timestamp: datetime


class SpendingRequest(BaseModel):
    points: int


class SpendingResponse(BaseModel):
    spendings: list


class BalanceResponse(BaseModel):
    balances: dict
