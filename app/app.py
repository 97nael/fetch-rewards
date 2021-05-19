from fastapi import FastAPI
from controllers.transactionController import trans_router


app = FastAPI()

app.include_router(trans_router)
