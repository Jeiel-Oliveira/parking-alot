from fastapi import APIRouter, Depends

from src.dto.reservationDto import ReservationDto
from src.service.reservation_service import ReservationService
from src.repository.reservation_repository import ReservationRepository
from src.database.mysql_connection import get_database_connection


def get_reservation_service():
    return ReservationService(
        ReservationRepository(get_database_connection())
    )


reservation_router = APIRouter(prefix="/parking")


@reservation_router.get("/")
def find_all(
    reservation_service: ReservationService = Depends(
        get_reservation_service
    ),
):
    return reservation_service.find_all()


@reservation_router.post("/")
def create(
    reservationDto: ReservationDto,
    reservation_service: ReservationService = Depends(
        get_reservation_service
    ),
):
    return reservation_service.create(reservationDto)


@reservation_router.get("/{reservation_id}")
def find_by_id(
    reservation_id: int,
    reservation_service: ReservationService = Depends(
        get_reservation_service
    ),
):
    return reservation_service.find_by_id(reservation_id)


@reservation_router.delete("/{reservation_id}")
def delete_by_id(
    reservation_id: int,
    reservation_service: ReservationService = Depends(
        get_reservation_service
    ),
):
    reservation_service.delete(reservation_id)
    return f"Deleted {reservation_id} successfully!"


@reservation_router.put("/{reservation_id}")
def update_by_id(
    reservation_id: int,
    reservationDto: ReservationDto,
    reservation_service: ReservationService = Depends(
        get_reservation_service
    ),
):
    return reservation_service.update(reservation_id, reservationDto)


class ReservationController:

    def __init__(self) -> None:
        self.router = reservation_router

    def get_router(self) -> APIRouter:
        return self.router
