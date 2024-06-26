
from typing import Union

from fastapi import FastAPI
from parking.controller.parking_controller import parking_controller

app = FastAPI()
app.include_router(parking_controller)


@app.get("/")
def read_root():
    return {"Server is running"}


@app.post("/")
def create_ticket():
    return "a"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


