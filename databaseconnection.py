import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
import psycopg2

@st.cache_resource
class DatabaseConnection:
    def connect_db(_self):
        _self.conn = psycopg2.connect(
            host=st.secrets["DB_HOST"],
            database=st.secrets["DB_DATABASE"],
            user=st.secrets["DB_USERNAME"],
            password=st.secrets["DB_PASSWORD"],
            port=st.secrets["DB_PORT"],
            sslmode=st.secrets["DB_SSLMODE"],
            connect_timeout=15,
            keepalives=1,
            keepalives_idle=30,
            keepalives_interval=10,
            keepalives_count=5)

    def main(self):
        self.connect_db()
        self.cursor = self.conn.cursor()