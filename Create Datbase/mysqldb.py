import mysql.connector

mydb = mysql.connector.connect(user='samkiller007', password='Incorrect@11',host='localhost',database='attendance')

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students")

for i in mycursor:
    print(i)