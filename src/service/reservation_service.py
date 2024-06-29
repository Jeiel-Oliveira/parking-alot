from src.repository.reservation_repository import ReservationRepository
from src.dto.reservationDto import ReservationDto
from src.model.reservation import Reservation

from src.exceptions.reservation_notfound_exception import (
    ReservationNotfoundException,
)


class ReservationService:
    reservation_repository: ReservationRepository

    def __init__(self, reservation_repository: ReservationRepository):
        self.reservation_repository = reservation_repository

    def find_all(self):
        reservations = self.reservation_repository.find_all()
        return reservations

    def create(self, reservationDto: ReservationDto):
        reservation = Reservation(
            start_time=reservationDto.start_time,
            end_time=reservationDto.end_time,
            status=reservationDto.status,
            price=reservationDto.price,
        )

        self.reservation_repository.create(reservation)
        return reservation

    def find_by_id(self, reservation_id: str):
        reservation = self.reservation_repository.find_by_id(
            reservation_id
        )

        if reservation is None:
            raise ReservationNotfoundException(reservation_id)

        return reservation

    def delete(self, reservation_id: str) -> bool:
        return self.reservation_repository.delete_by_id(reservation_id)

    def update(self, reservation_id, reservationDto: ReservationDto):
        reservation = Reservation(
            reservation_id=reservation_id,
            start_time=reservationDto.start_time,
            end_time=reservationDto.end_time,
            status=reservationDto.status,
            price=reservationDto.price,
        )

        return self.reservation_repository.update(reservation)
