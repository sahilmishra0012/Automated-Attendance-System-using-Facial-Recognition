# Automated-Attendance-System-using-Facial-Recognition

Automated-Attendance-System of face detection and recognition is to present face recognition in real time environment for educational institutes or an organization to see and mark the attendance of their students or employees on a daily basis to keep track of their presence.

Why and How we are going to approach?
Attendance management system is a necessary tool for taking attendance in any environment where attendance is critical. However, most of the existing approach are time consuming, intrusive and it require manual work from the users. This project is aimed at developing a less intrusive, cost effective and more efficient automated student attendance management system using face recognition that leverages on SAS cloud computing (CC) infrastructure. It takes attendance by using IP camera mounted in front of a classroom, to acquire images of the entire class. It detect the faces in the image and compares it with the enrolled faces in the database. On identification of a registered face on the acquired image collections, the attendance register is marked as present otherwise absent.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

The Python libraries needed for this project are in requirement.txt files. These libraries can be easily installed using pip over requirement.txt. 

### Installing

A step by step series of examples that tell you how to get a development env running

To get all the necessary libraries install anaconda. Almost all the dependencies are available in the anaconda itself. 

Download keras facenet model and their weights as they are alredy trained on billions of images for face recognition. This model will help in extracting the embedding of faces present in the images.

Install OpenCV for python using folowing commands:


End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

face_detect_video.py file detects the faces captured from webcam.
image_embedding.py file generates the embedding of faces in the images.


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

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

