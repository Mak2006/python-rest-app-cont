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

### What was done 

1. We install virtualenv, create a directory for the env and install Flask in it. Flasks installs the core components flask, Werkzeug, Jinja2, click, itsdangerous, and markupsafe.
2. We create a small Flask server `server.py`
	1. Debug - enabled 
	2. 
1. We create a separate configuration file 'myconfig.cfg' and load it via  `app.config.from_pyfile('myconfig.cfg') `
1. 






