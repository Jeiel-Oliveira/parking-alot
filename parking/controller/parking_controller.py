from fastapi import APIRouter
from parking.repository.parking_repository import ParkingRepository
from parking.database.mysql_connection import MysqlConnection

router = APIRouter(prefix='/parking')

sqlite_connection = MysqlConnection()
sqlite_connection.connect()

print(sqlite_connection.conn)


@router.get("/")
def find_parkings():
    parking_repository_imp = ParkingRepository(sqlite_connection.conn)
    return parking_repository_imp.find_all()
