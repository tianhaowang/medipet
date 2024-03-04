import mysql.connector
import os

# Read the database credentials from environment variables
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

# Establish a connection to the MySQL database
def get_database_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

connection = get_database_connection()
cursor = connection.cursor()

query = "Delete from users"
cursor.execute(query)
connection.commit()
