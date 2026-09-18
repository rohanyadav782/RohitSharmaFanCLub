import os
from dotenv import load_dotenv

load_dotenv()
import psycopg2

class DatabaseConnection:
    def connect_db(_self):
        _self.conn = psycopg2.connect(
            host=os.getenv("db_host"),
            database=os.getenv("db_database"),
            user=os.getenv("db_user"),
            password=os.getenv("db_password"),
            port=os.getenv("db_port"),
            sslmode=os.getenv("db_sslmode"),
            connect_timeout=15,
            keepalives=1,
            keepalives_idle=30,
            keepalives_interval=10,
            keepalives_count=5)

    def main(self):
        self.connect_db()
        self.cursor = self.conn.cursor()