from pydantic import BaseModel


class ReservationDto(BaseModel):
    reservation_id: str = None
    start_time: str
    end_time: str
    status: str
    price: int  # in cents
