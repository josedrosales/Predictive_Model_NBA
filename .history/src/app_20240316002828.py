
import sqlalchemy
import os
import psycopg2
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password
    )

    # Crear un cursor para ejecutar consultas SQL
    cursor = connection.cursor()

    # Crear la base de datos si no existe
    cursor.execute("CREATE DATABASE IF NOT EXISTS NBA;")
    
except psycopg2.Error as error:
    print("Error al conectar o interactuar con la base de datos:", error)
