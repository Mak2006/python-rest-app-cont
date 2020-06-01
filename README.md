# python-rest-app-cont

# Aim of the application - Demo of a python based REST api microservices based applciation. 

## Architecture
A client server microservice based application. 

Client is web based UI, a flask based python microservice application. 

Server is a microservice which exposes a REST API.  The REST API documentation is using Swagger documentation. 
For now the service does not use a backend. 

##SDLC

The testing of the done using, The CI/CD is done using Jenkins. 

Containerization using docker and kubernetes. 


## Usage
The applicaiton is available for download at docker registry. 
The source code can be installed with the following command `xyz`

The source code of the application is available at github. 

## What was done 

### Installation of virtualenv and Flask, project set up. 
1. We install virtualenv, create a directory for the env and install Flask in it. Flasks installs the core components flask, Werkzeug, Jinja2, click, itsdangerous, and markupsafe.
2. Create Github and load the project in PyCharm. 

### Create a configuratioin for the project so that we can handle prod, preprod, staging, dev environments. 
1. At a small scale we create a small Flask server `server.py` and have Debug - enabled 
1. We create a separate configuration file 'myconfig.cfg' and load it via  `app.config.from_pyfile('myconfig.cfg') `
1. In this case include a Configuration Object itself. This is handled by `configuration.py`. We load it using `






