import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",user="root", password=""
)

mycursor = mydb.cursor()
try:
    mycursor.execute("""
        CREATE DATABASE IF NOT EXIST alx_book_store
    """)
except mysql.connector.Error as e:
    print("Error: Database already exist")

print("Database 'alx_book_stor' created successfully")
mycursor.close()
mydb.close()