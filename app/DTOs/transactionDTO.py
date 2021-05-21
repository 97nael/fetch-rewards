from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict


class TransactionRequest(BaseModel):
    payer: str
    points: int
    timestamp: datetime


class SpendingRequest(BaseModel):
    points: int


class SpendingResponse(BaseModel):
    spendings: List = []


class BalanceResponse(BaseModel):
    balances: Dict[str, int] = {}
