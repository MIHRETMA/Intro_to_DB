# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server (not to a specific database yet)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='ALXB$3d13100$'
    )

    cursor = connection.cursor()

    # Try to create the database
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

    # Clean up
    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
