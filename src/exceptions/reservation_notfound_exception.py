from fastapi import HTTPException


class ReservationNotfoundException(HTTPException):

    def __init__(self, reservation_id: str):
        super().__init__(
            status_code=404,
            detail=f"Reserva com o ID {reservation_id} não encontrada",
        )
