import os

from fastapi import FastAPI

from app.crud import Crud
from app.web3_client import get_w3

w3 = get_w3(os.getenv("WEB3_PROVIDER"))
crud = Crud(os.getenv("DB_URI"))


app = FastAPI()


@app.get("/addresses/{address}")
async def find_balances(address: str):
    return {"message": "To be implemented."}


@app.get("/session/{id}")
async def get_session(id: str):
    return {"message": "To be implemented."}
