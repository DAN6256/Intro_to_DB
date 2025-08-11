import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",user="root", password=""
    )
except mysql.connector.Error as e:
    print("Error: Unable to connect", e)

mycursor = mydb.cursor()

mycursor.execute("""
        CREATE DATABASE IF NOT EXISTS alx_book_store
""")


print("Database 'alx_book_stor' created successfully")
mycursor.close()
mydb.close()