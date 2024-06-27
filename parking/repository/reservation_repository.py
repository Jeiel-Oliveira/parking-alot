from mysql.connector import connection
from parking.model.reservation import Reservation


class ReservationRepository:
    table: str = "RESERVATIONS"

    connection: connection.MySQLConnection

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

    def __init__(self, connection):
        self.connection = connection

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

        return cursor.rowcount

    def find_by_id(self, reservation_id: str):
        cursor = self.connection.cursor()
        cursor.execute(
            f"SELECT * FROM {self.table} WHERE reservation_id=" + str(reservation_id)
        )

        reservation = cursor.fetchone()
        cursor.close()

        return reservation

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

    def find_all(self):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table}")
        reservations = cursor.fetchall()
        cursor.close()

        return reservations
