import os
from parking.database.db_connection import DbConnection
from mysql.connector import (connection)


class MysqlConnection(DbConnection):
    conn: connection.MySQLConnection = None

    def __init__(self):
        super().__init__()

    def connect(self):
        if not self.conn:
            self.conn = connection.MySQLConnection(
                host="127.0.0.1",
                database="parking_alot",
                user="parking",
                password="parking"
                # user=os.getenv('MYSQL_USER'),
                # password=os.getenv('MYSQL_PASSWORD'),
                # host=os.getenv('MYSQL_HOST'),
                # database=os.getenv('MYSQL_DATABASE')
            )

    def disconnect(self):
        self.conn.close()
