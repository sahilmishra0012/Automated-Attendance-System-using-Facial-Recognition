import mysql.connector
import sys
import numpy as np
sys.path.insert(1, '/home/samkiller007/Downloads/Projects/Machine Learning/Automated Attendance System/Face Detection/')
import image_embedding

mydb = mysql.connector.connect(user='samkiller007', password='Incorrect@11',host='localhost',database='attendance')

mycursor = mydb.cursor()

path='/home/samkiller007/Downloads/Projects/Machine Learning/Automated Attendance System/Dataset/Images'
embeddings=image_embedding.generate_image_encoding(path)


embeddings=embeddings.tolist()
roll=input('Enter Roll Number')
stud_name=input('Enter Name')

query="INSERT into students values(\'"+str(roll)+"\',\'"+str(stud_name)+"\',\'"+str(embeddings)+"\')"
mycursor.execute(query)
mydb.commit()

