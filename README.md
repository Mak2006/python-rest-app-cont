# python-rest-app-cont

# Aim of the application 
**Demo of a python based REST api microservices based applciation.**
The application adds two numbers and returns the result. The UI is intended as the first microservice and the backend as the second one.  

## Stages of the application dev and SDLC - overall follow a **TDD** and agile approach
1. Stage 1 - Create a monolith and implement the fuctionality. 
2. Stage 2 - Dissect the application into two microservices, add swagger documentation for REST API.
3. Stage 3 - Containerize the applicaition and host on Docker or Heroku

## Current status of application 
1. Stage 1 WIP	
2. Libraries used  - Flask, jq, virtualenv, pytest, tox, 

## Target Architecture
A client server microservice based application. 
Client is web based UI, a flask based python microservice application. 
Server is a microservice which exposes a REST API.  The REST API documentation is using Swagger documentation. 
For now the service does not use a backend. 

## Usage
The source code of the application is available at github. 
Install Python, Flask and run the `server.py`

## What was done 
### virtualenv and Flask, pytest, jq project were set up. 
1. We install virtualenv, create a directory for the env and install Flask in it. Flasks installs the core components flask, Werkzeug, Jinja2, click, itsdangerous, and markupsafe.
2. Create Github repo and load the project in PyCharm. 

### Create a configuration for the project so that we can handle prod, preprod, staging, dev environments. 
1. At a small scale we create a small Flask server `server.py` and have Debug - enabled 
1. We create a separate configuration file 'myconfig.cfg' and load it via  `app.config.from_pyfile('myconfig.cfg') `
1. In this case include a Configuration Object itself. This is handled by `configuration.py`. We load it using `app.config.from_object('configuration.DevelopmentConfig')`. We change the `server.py` to include this.
1. With debug on we made some changes to `server.py` and refresh the browser. We are able to see the changes.

### Project organization 
1. We use the generic directory structure, our app is mathapp and a module, tests are separated, 
```
mathapp/
    - server.py  # serves a monolith , contain view, model
    - configuration.py 
    - __init__.py 
    - static/ 
       - home.html  # our landing page
tests/            
    - functional  
    - unit
```
1. we create the `__init__.py` empty file, so that we can treat `mathapp` as a moudle

### Test run the application. 
`python server.py` launces this and the application would be available at the stock URL 
![enter image description here](https://i.imgur.com/rPo5m1T.png)

### Enhance the UI 
The UI at present has no authentication or authorisation, it is a simple mechnism to obtain some input and call the rest service exposed and get the response.  This is merely achived by including a home.html which serves as the landing page of our application. We change it and we add a welcome note and add a form.
At this stage our application is ![App](https://i.imgur.com/w5yGfU3.png)

### The REST backend layer and the model
At this stage it is a monolith and in the same `server.py` we create our service and model. 
We add the HTTP POST handlers. This is the part where the REST api is created. 
A add method is created. It is exposed as as POST method using `@app.route('/mathapp/api/v1.0/add', methods=['POST'])`. The input parameters are obtained via `a = request.json.get('number1', 0);` where `number1` matches the input field. The data is then converted to floats. Then the result is then returned via jsonify object

### Testing the `add` service layer. We do the following test
1. Using curl to post a message. 
`curl -i -H "Content-Type: application/json" -X POST -d '{"number1":"20", "number2":"30", "number3":"40"}' http://127.0.0.1:5000/mathapp/api/v1.0/add`

Firing a few curls gives the result below 
![res](https://i.imgur.com/rETQRdq.png)


### TDD 
At this stage we are ripe enough to introduce TDD. We use pytest rather than the built in `unittest` as pytest does more, and already have it installed. pytest would auto discover the tests from file prefixed with `test_`. We further keep our functional and unit tests separate. 

### Adding the functional tests. 
1. functional - we add two tests 
	1. **404 response test** We want to show a custom 404 page if there is a client error. So we create a test for this.
	2. **Response shown test** - we want to make sure a response is actually being shown to the user.
At this stage both our`pytest` fails. 
![](https://i.imgur.com/QgGbIcc.png)


After adding the code for 404 and 500, we now have added custom error pages as below. `pytest` also passes. The custom 500 error page. 
<kbd>![500](https://i.imgur.com/nKmVTpW.png) </kbd>

Now before we move on to doing a few more tests, we include logging
### Adding Logging 



		
1. unit 
	1. `add` service throws proper error on incorrect input, 
	1. The method computes the sum correctly. 

### Error handling 
1. We now add custom 4xx and 5xx error handling. 
2. We tackle conversion errors. 



### Exposing the documentation for the REST layer



### Adding basic security

### Marrying the UI with the REST service

### Deploy and check the application 
1. using curl with jq
2. using the view layers

### Next steps, 
1. partition the application into separate microservices 
1. Make the application ready for containerization. 
1. use docker and k8s for containerization. 
2. set up Jenkins for auto packaging and release. 
1. Push the images to docker unofficial repo









