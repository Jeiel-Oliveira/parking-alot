from datetime import datetime


class Reservation:
    reservation_id: int
    start_time: datetime
    end_time: datetime
    status: str
    price: int  # in cents

    def __init__(
        self,
        start_time: str,
        end_time: str,
        status: str,
        price: int,
        reservation_id: int = None,
    ):
        self.reservation_id = reservation_id
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.price = price

    @staticmethod
    def from_dict_factory(reservation_dict: dict):
        return Reservation(
            reservation_id=reservation_dict["reservation_id"],
            start_time=reservation_dict["start_time"],
            end_time=reservation_dict["end_time"],
            status=reservation_dict["status"],
            price=reservation_dict["price"],
        )
