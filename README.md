# Automated-Attendance-System-using-Facial-Recognition

Automated Attendance System leverages the power of face detection and recognition for institution and organizations to see and mark the attendance of their students or employees on a daily basis and keep track of their presence.

Why and How we are going to approach?   
Attendance Management System is a necessary tool for marking attendance in any environment where attendance is critical. However, most of the existing approach are time consuming, intrusive and it require manual work from the users. This project is aimed at developing a less intrusive, cost effective and more efficient automated student attendance management system using face recognition that leverages on SAS cloud computing (CC) infrastructure. It takes attendance by using the smartphone camera to acquire images of people. It detect the faces in the image and compares it with the images of enrolled people in the database. On identification of a registered face on the acquired image collections, the attendance register is marked as present otherwise absent.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The Python libraries needed for this project are in requirement.txt files. These libraries can be easily installed using pip over requirement.txt. 

### Installing

To get all the necessary libraries install [Anaconda](https://www.anaconda.com/). Almost all the dependencies are available in the anaconda itself. 

Download [Keras-FaceNet](https://drive.google.com/drive/folders/1pwQ3H4aJ8a6yyJHZkTwtjcL4wYWQb7bn) model and their weights as they are alredy trained on billions of images for facial recognition. This model will help in extracting the embedding of faces present in the images.

Install [OpenCV](https://pypi.org/project/opencv-python/) for python using folowing command:

```
$ pip install opencv-python
```

## Directory Structure

    --client
        --static
            --img
                (Images for the Front-End)
        --flaskapp.py
            (Flask Application for App Deployment)
        --mobile.html
            (First Page of Web App)
        --notfound.html
            (Rendered when Student is not in database)
        --present.html
            (Rendered when Student is marked present)
        --ngrok
            (Tunnelling App to run localhost public IP)
    --Create Datbase
        --create_database.py
            (Script to save students' data in database)
    --Dataset/Images
        (Saves the captured image temporarily for face recognition)
    --Face Detection
        --face_detect_video.py
            (Script to detect faces in webcam videos)
        --face_detect.py
            (Script contains functions to extract faces from images)
        --haarcascade_frontalface_default.xml
            (OpenCV Classifier to extract faces)
        --image_preprocess.py
            (Script to make image ready for embedding extraction)
        --image_embedding.py
            (Script to extract embedding vectors of faces in images)
    --Face Matching
        --similarity.py
            (Contains functions to get similarity between faces in images)
        --db_extraction.py
            (Script to fetch students from database and mark the attendance)
    --README.md
        (README for the following project)
    --requirements.txt
        (Consists of python dependecies required to run the code)


## Deployment

The following code is deployed on the ```https://localhost:8080``` and is made public on a URL using ```ngrok``` to access it remotely on the smartphones for easier handling.

## Authors

* [**Sahil Mishra**](https://github.com/sahilmishra0012)
* [**Shubham Negi**](https://github.com/negishubham3503)
* [**Abhishek Singh**](https://github.com/abhishekaashu)
