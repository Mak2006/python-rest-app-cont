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
1. In this case include a Configuration Object itself. This is handled by `configuration.py`. We load it using `app.config.from_object('configuration.DevelopmentConfig')`. Altered the `server.py` to include this.
1. With debug on we made some changes to `server.py` and refresh the browser. We are able to see the changes.

### Project organization 
1. We use the generic Flask based structure and adopt structure which can be enhanced in the future. 

```
my_app/ 
    - app.py 
    - config.py 
    - __init__.py 
    - static/ 
       - css/ 
        - js/ 
        - images/ 
            - home.png 
```

### We now build the UI layers
The UI at present has no authentication or authorisation, it is a simple mechnism to obtain some input and call the rest service exposed and get the response. ** At this stage** the back end is not done so we mock the rest layer and test it. 

### The testing debugging the UI layer. 


### The REST backend layer and the model

### The testing debugging the UI layer. 

### Exposing the documentation for the REST layer

### Deploy and check the application 
1. using curl with jq
2. using the view layers

### Next steps, 
1. partition the application into separate microservices 
1. Make the application ready for containerization. 
1. use docker and k8s for containerization. 
2. set up Jenkins for auto packaging and release. 
1. Push the images to docker unofficial repo









