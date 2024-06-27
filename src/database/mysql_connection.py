from src.database.db_connection import DbConnection
import mysql.connector

def get_database_connection():
    connection = MySqlConnection()
    connection.connect()
    return connection.conn


class MySqlConnection(DbConnection):
    conn: mysql.connector.connect = None

    def __init__(self):
        super().__init__()

    def connect(self):
        if not self.conn:
            self.conn = mysql.connector.connect(
                host="mysql-parking",
                database="parking_alot",
                user="parking",
                password="parking"
            )

    def disconnect(self):
        self.conn.close()
