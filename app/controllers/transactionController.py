from fastapi import APIRouter
from models.transactionModel import (
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
    pass


@trans_router.post("/spend", response_model=SpendingResponse)
def spend_points(spendings: SpendingRequest):
    pass


@trans_router.get("/balance", response_model=BalanceResponse)
def get_payer_balances():
    pass
