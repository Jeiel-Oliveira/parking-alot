from fastapi import APIRouter
from parking.repository.reservation_repository import ReservationRepository
from parking.database.mysql_connection import MySqlConnection
from parking.dto.reservationDto import ReservationDto
from parking.model.reservation import Reservation

reservation_router = APIRouter(prefix="/parking")

sqlite_connection = MySqlConnection()
sqlite_connection.connect()

reservation_repository = ReservationRepository(sqlite_connection.conn)


@reservation_router.get("/")
def find():
    return reservation_repository.find_all()


@reservation_router.post("/")
def create(reservationDto: ReservationDto):
    reservation = Reservation(
        start_time=reservationDto.start_time,
        end_time=reservationDto.end_time,
        status=reservationDto.status,
        price=reservationDto.price,
    )

    reservation_repository.create(reservation)
    return reservation


@reservation_router.get("/{reservation_id}")
def find_by_id(reservation_id: int, q: str = None):
    reservation = reservation_repository.find_by_id(reservation_id)
    return reservation


@reservation_router.put("/{reservation_id}")
def update_by_id(reservation_id: int, reservationDto: ReservationDto):
    reservation = Reservation(
        reservation_id=reservation_id,
        start_time=reservationDto.start_time,
        end_time=reservationDto.end_time,
        status=reservationDto.status,
        price=reservationDto.price,
    )

    reservation_repository.update(reservation)

    return reservation
