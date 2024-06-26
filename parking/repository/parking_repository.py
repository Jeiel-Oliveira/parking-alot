from mysql.connector import (connection)


class ParkingRepository:

    table: str = "PARKING"

    connection: connection.MySQLConnection

    def __init__(self, connection):
        self.connection = connection

    def find_all(self):
        cursor = self.connection.cursor()
        parkings = cursor.execute(f"SELECT * FROM {self.table}")
        print(parkings)

