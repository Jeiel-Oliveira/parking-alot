from parking.database.db_connection import DbConnection
import mysql.connector


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
                # user=os.getenv('MYSQL_USER'),
                # password=os.getenv('MYSQL_PASSWORD'),
                # host=os.getenv('MYSQL_HOST'),
                # database=os.getenv('MYSQL_DATABASE')
            )

    def disconnect(self):
        self.conn.close()
