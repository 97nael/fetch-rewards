"""
API endpoints for actions related to points and transaction requests
"""

from fastapi import APIRouter
import services.transactionServices as tS
from DTOs.transactionDTO import (
    TransactionRequest,
    SpendingRequest,
    SpendingResponse,
    BalanceResponse
)


trans_router = APIRouter(
    responses={404: {"Description": "Not found"}}
)


@trans_router.post("/add", status_code=201)
def add_transaction(tranaction: TransactionRequest):
    tS.add_transaction(tranaction)


@trans_router.post("/spend", response_model=SpendingResponse)
def spend_points(spendings: SpendingRequest):
    return tS.spend_points(spendings)


@trans_router.get("/balance", response_model=BalanceResponse)
def get_payer_balances():
    return tS.get_balances()
