# python-rest-app-cont

# Aim of the application 
**Demo of a python based REST api microservices based applciation. The application adds two numbers and returns the result. The UI is intended as the first microservice and the backend as the second one.  **

## Stages of the application
1. Stage 1 - Create a monolith and implement the fuctionality. 
2. Stage 2 - Dissect the application into two microservices, add swagger documentation for REST API.
3. Stage 3 - Containerize the applicaition and host on Docker or Heroku

## Current status of application 
1. Stage 1 WIP
	

## Final Architecture
A client server microservice based application. 
Client is web based UI, a flask based python microservice application. 
Server is a microservice which exposes a REST API.  The REST API documentation is using Swagger documentation. 
For now the service does not use a backend. 

## Usage
The source code of the application is available at github. 
Install Python, Flask and run the server.py

## What was done 

### Installation of virtualenv and Flask, project set up. 
1. We install virtualenv, create a directory for the env and install Flask in it. Flasks installs the core components flask, Werkzeug, Jinja2, click, itsdangerous, and markupsafe.
2. Create Github repo and load the project in PyCharm. 

### Create a configuratoin for the project so that we can handle prod, preprod, staging, dev environments. 
1. At a small scale we create a small Flask server `server.py` and have Debug - enabled 
1. We create a separate configuration file 'myconfig.cfg' and load it via  `app.config.from_pyfile('myconfig.cfg') `
1. In this case include a Configuration Object itself. This is handled by `configuration.py`. We load it using `app.config.from_object('configuration.DevelopmentConfig')`. We change the `server.py` to include this.
1. With debug on we made some changes to `server.py` and refresh the browser. We are able to see the changes.

### Project organization 
1. We use the generic Flask based structure and adopt structure which can be enhanced in the future. 

```
my_app/ 
    - server.py 
    - configuration.py 
    - __init__.py 
    - static/ 
       - home.html  # our landing page
       - css/ 
        - js/ 
        - images/ 
            - home.png 
```
1. we create the __init__.py file, so that we can treat it as moudle

### Test run the application. 
`python server.py` launces this and the application would be available at the stock URL 
![enter image description here](https://i.imgur.com/rPo5m1T.png)

### Enhance the UI 
The UI at present has no authentication or authorisation, it is a simple mechnism to obtain some input and call the rest service exposed and get the response.  This is merely achived by including a home.html which serves as the landing page of our application. 

Changes we make are 
1. We add a welcome note and add a form.
At this stage our application is ![App](https://i.imgur.com/w5yGfU3.png)

2. We then add teh post handlers.

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









