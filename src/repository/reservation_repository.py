from collections import namedtuple

from mysql.connector import MySQLConnection
from src.model.reservation import Reservation

class ReservationRepository:
    table: str = "RESERVATIONS"
    connection: MySQLConnection

    def __init__(self, connection):
        self.connection = connection

    def generate_reservation_factory(self, reservation_dict: dict) -> Reservation:
        return Reservation.from_dict_factory(reservation_dict)


    def create_table(self):
        """
        CREATE TABLE RESERVATIONS (
            reservation_id INT PRIMARY KEY AUTO_INCREMENT,
            start_time TIMESTAMP NOT NULL,
            end_time TIMESTAMP NOT NULL,
            status VARCHAR(20) NOT NULL,
            price INT NOT NULL
        );
        """


    def create(self, reservation: Reservation):
        cursor = self.connection.cursor()
        sql = (
            f"INSERT INTO {self.table} "
            "(start_time, end_time, status, price) "
            "VALUES (%s, %s, %s, %s)"
        )

        cursor.execute(
            sql,
            (
                reservation.start_time,
                reservation.end_time,
                reservation.status,
                reservation.price,
            ),
        )
        self.connection.commit()
        cursor.close()

    def delete_by_id(self, reservation_id: int):
        cursor = self.connection.cursor()
        cursor.execute(
            f"DELETE FROM {self.table} WHERE reservation_id= " + str(reservation_id)
        )

        self.connection.commit()
        cursor.close()

        return cursor.rowcount > 0

    def find_by_id(self, reservation_id: str):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(
            f"SELECT * FROM {self.table} WHERE reservation_id=" + str(reservation_id)
        )

        reservation = cursor.fetchone()
        cursor.close()

        return self.generate_reservation_factory(reservation)

    def find_all(self):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {self.table}")
        reservations = cursor.fetchall()
        cursor.close()

        return list(map(self.generate_reservation_factory, reservations))

    def update(self, reservation: Reservation):
        cursor = self.connection.cursor()

        sql = (
            f"UPDATE {self.table} "
            "SET start_time = %s, end_time = %s, status = %s, price = %s "
            "WHERE reservation_id = %s"
        )

        cursor.execute(
            sql,
            (
                reservation.start_time,
                reservation.end_time,
                reservation.status,
                reservation.price,
                reservation.reservation_id,
            ),
        )
        self.connection.commit()
        cursor.close()
