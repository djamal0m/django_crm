import mysql.connector

myDb = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    passwd= 'root1234',
)

cursorObject = myDb.cursor()
cursorObject.execute('CREATE DATABASE django_crm')
print("ALL DONE!")