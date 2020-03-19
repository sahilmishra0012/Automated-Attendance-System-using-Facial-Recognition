import mysql.connector
import numpy as np
from similarity import calc_dist

def get_student(emb):

    mydb = mysql.connector.connect(user='samkiller007', password='HeloWord',host='localhost',database='attendance')

    mycursor = mydb.cursor()

    query="SELECT * FROM students"
    mycursor.execute(query)
    for i in mycursor:
        p=list(i[2].split(','))
        p[0]=p[0][1:]
        p[-1]=p[-1][:-1]
        k=[float(i) for i in p]
        dist=calc_dist(k,emb)
        if dist<1:
            return i[0],i[1]
    return 'Not Found','Not Found'
