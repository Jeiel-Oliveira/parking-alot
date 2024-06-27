from fastapi import FastAPI
from parking.controller.reservation_controller import reservation_router

app = FastAPI()


@app.get("/")
def read_root():
    return "Server is running"


app.include_router(reservation_router)
