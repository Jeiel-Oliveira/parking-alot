from fastapi import FastAPI, HTTPException
from src.controller.reservation_controller import ReservationController
from src.exceptions.exception import http_exception_handler

app = FastAPI()


@app.get("/")
def read_root():
    return "Server is running"


reservation_routes = ReservationController().get_router()

app.add_exception_handler(HTTPException, http_exception_handler)

app.include_router(reservation_routes)
