from DTOs.transactionDTO import (
    TransactionRequest,
    SpendingRequest,
    SpendingResponse,
    BalanceResponse
)
from utils.storage import create_storage, sort_storage


mem_storage = create_storage()


def add_transaction(transaction: TransactionRequest):
    global mem_storage

    mem_storage.append(transaction)


def spend_points(spendings: SpendingRequest):
    global mem_storage
    mem_storage = sort_storage(mem_storage)

    points = spendings.points
    res = SpendingResponse()

    total_spend = 0

    while len(mem_storage) > 0 and points > 0:
        transaction = mem_storage.pop(0)
        payout = transaction.points

        points -= payout

        if points < 0:
            payout = transaction.points + points

            transaction.points = abs(points)
        else:
            transaction.points = 0

        res.spendings.append(
            {
                "payer": transaction.payer,
                "points": -payout
            }
        )

        mem_storage.append(transaction)

    ind = 0

    while ind < len(res.spendings):
        points = res.spendings[ind]["points"]

        if points > 0:
            temp = res.spendings.pop(ind) 
            ind2 = 0

            while ind2 < len(res.spendings):
                if res.spendings[ind2]["payer"] == temp["payer"]:
                    res.spendings[ind2]["points"] += temp["points"]

                    if res.spendings[ind2]["points"] <= 0:
                        break
                    else:
                        temp = res.spendings.pop(ind2)
                else:
                    ind2 += 1
        else:
            ind += 1

    return res


def get_balances():
    global mem_storage

    mem_storage = sort_storage(mem_storage)
    res = BalanceResponse()

    for item in mem_storage:
        if item.payer not in res.balances:
            res.balances[item.payer] = 0

        res.balances[item.payer] += item.points

    return res
