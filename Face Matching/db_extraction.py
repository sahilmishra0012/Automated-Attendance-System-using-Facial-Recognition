import mysql.connector
from similarity import calc_dist

def get_student(emb):

    mydb = mysql.connector.connect(user='samkiller007', password='Incorrect@11',host='localhost',database='attendance')

    mycursor = mydb.cursor()

    query="SELECT * FROM students"
    mycursor.execute(query)
    for i in mycursor:
        k=calc_dist(i[3],emb)
        if k<1:
            return i[0],i[1]
