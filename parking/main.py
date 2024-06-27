from fastapi import FastAPI
from parking.controller.reservation_controller import ReservationController

app = FastAPI()


@app.get("/")
def read_root():
    return "Server is running"


reservation_routes = ReservationController().get_router()


app.include_router(reservation_routes)
