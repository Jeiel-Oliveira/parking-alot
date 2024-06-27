from fastapi import FastAPI
from parking.controller.reservation_controller import reservation_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Server is running"}


@app.get("/health")
def server_health():
    return {"Server is health"}


app.include_router(reservation_router)
