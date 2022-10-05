<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="UE AD A1 REST" />
</div>

<h1 align="center">UE AD A1 REST</h1>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#dart_check_mark-Structure Of the project">Structure of the project</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

This is a simple microservice application to manage movies reservation implemented using Flask, REST and gRPC technology
## :sparkles: Features ##

:heavy_check_mark: CRUD for movies reservation


## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Docker](https://www.docker.com/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Python](https://www.python.org/), [Pipe](https://pypi.org/project/pip/) and [Docker](https://www.docker.com/) installed.


## :dart: Structure Of the project ##

The application is divided into 4 microservies (Booking, Showtimea and Movie implemented using gRPC, and User implementend using REST). 
Each folder contains a :
  - Python implementation of the microservice using gRPC/REST 
  - Service_pb2_grpc.py and service_pb2.py : generated python files from the proto file (in case it is a gRPC service)
  - Other X_pb2_grpc.py and X_pb2.py files (in case the service request other gRPC service)
  - Proto file that contains the methods offered by the service (in case it is a gRPC service)
  - A json file as a database.
  - A Requirement file and a Dockerfile to create a docker image for the service
  - The OpenApi specification for the service (in case it is a REST service)
```
UE-AD-A1-REST
│   README.md
│   docker-compose.yml
│   file.py
│   LICENSE
│   requirements.txt  
│
│ 
└───booking
│   │   booking.py
│   │   Dockerfile
│   │   requirements.txt
│   │
│   └───data
│   │   │   bookings.json
│   │   │
│   └───protos
│       │   booking.proto
│   
│ 
└───movie
│   │   movie.py
│   │   Dockerfile
│   │   requirements.txt
│   │
│   └───data
│   │   │   movies.json
│   │   │
│   └───protos
│       │   movie.proto
│   
│ 
└───showtime
│   │   showtime.py
│   │   Dockerfile
│   │   requirements.txt
│   │
│   └───data
│   │   │   times.json
│   │   │
│   └───protos
│       │   showtime.proto
│   
│ 
└───user
│   │   user.py
│   │   Dockerfile
│   │   requirements.txt
│   │
│   └───data
│       │   user.json
```

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/MohammedAymane/UE-AD-A1-REST

# Access
$ cd ue-ad-a1-rest

# Install dependencies
$ pip -r requirements.txt

# Run a specific microservice (movie for example)
$ cd movie
$ python movie.py
$ pymon movie.py (in developpment mode)


# The movie service will initialize in the <http://localhost:3200>
```
## :checkered_flag: Containerizing the application ##
```bash
# Creating the containers
$ cd movie
$ docker build .

# Running the containers
$ cd UE-AD-A1-REST
$ docker-compose up

```

## :memo: License ##

This project is under license from MIT.


Authors : OUGGADI Mohammed-Aymane - MAKNI Sonda

&#xa0;

<a href="#top">Back to top</a>
