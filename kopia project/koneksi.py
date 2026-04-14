import mysql.connector

def koneksi():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kopiadb"
    )
    return db