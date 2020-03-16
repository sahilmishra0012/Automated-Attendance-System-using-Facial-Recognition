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
```face_detect_video.py``` file detects the faces captured from webcam.
```image_embedding.py``` file generates the embedding of faces in the images.


## Deployment

Add additional notes about how to deploy this on a live system

The following code is deployed in the WebApp on using ngrok.

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

