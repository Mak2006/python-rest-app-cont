# python-rest-app-cont

# Aim of the application 
**Demo of a python based REST api microservices based applciation.**
The application adds two numbers and returns the result. The UI is later intended to be the first microservice and the backend as the second one.  

##Requirements 
Creat a Python client server applicaton that takes in two numbers and returns the result. 

## Assumptions made
1. On Requirements - 
	1. The API will be callable by both curl and UI. 
	1. The API will accept only default application/x-www-form-urlencoded method.
	1. The input data requires to be checked for null, wrong values
	1. Proper error will be shown for 4xx,5xx
	1. The UI will not retain the values after it computes the addition. 
	1. The API will show proper message if improper data is supplied.
	1. Basic error handling and logging is required. 
1. Architecture - 
	1. Single app, no load balancing and production level features like security.
	2. No authentication, authorization is required. 
	2. No CI/CD, containerization is required
	1. The app is not required to be packaged. 
	
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


##Stage 1 - status WIP
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
**Note** at this stage we are using json, we have removed this later. 

### TDD 
At this stage, we start with TDD, ** that is do the tests first and then develop**. We use pytest rather than the built in `unittest` as pytest does more, and already have it installed. pytest would auto discover the tests from file prefixed with `test_`. We further keep our functional and unit tests separate. 

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
For this we do not use any additional libraries and use the built in logging and add the code below to `server.py`
```
    handler = FileHandler('C:\log\mathapp.log')
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(filename)s:%(lineno)d]'
    ))
    app.logger.addHandler(handler)
    app.logger.info("*** App started ")
    app.logger.info('Log test info')

```
### TDD continued - implmenting the core functional test
We resume the core functional test which is to make sure a result is acutally displayed, this is our test `test_page_response()` in the `test_func.py` The form is changed to send the result using `   return render_template('home.html', Result=result )`. The `home.html` now has the display usin `{{Result}}`.
![](https://i.imgur.com/GfzLMzO.png)

### TDD continued - unit tests
We now check if the service would work correctly in all , specifically
1. `sum` service throws proper error on incorrect input, 
1. The method computes the sum correctly. 
We add the following unit test assertions in `test_unit.py`
```
def test_sum():
    nulldata1 = [None, None]
    strdata2 = ["a", "b", "c"]
    nulllist = []

    result = str(sum(nulldata1))
    assert "Cannot add null data" == result

    result = str(sum(strdata2))
    assert "Cannot add str data" == result

    result = str(sum(nulllist))
    assert "Cannot add empty list" == result

```

Right now if we supply empty data from UI we see the following. 
<kbd>![Server cant handle null](https://i.imgur.com/WrSU5wi.png)</kbd>

The pytests are also failing as the `sum()` does no input checking
![sum service is failing](https://i.imgur.com/PE9NCiG.png)

*So our tests are now created and we start developing*


This completes the first Stage of the project.

## Stage 2 - TBD
1. Exposing the documentation for the REST layer
1. Adding basic authentication

## Stage 3 - TBD
1. Partition the application into separate microservices 
1. Make the application ready for containerization. 
1. set up Jenkins for auto packaging and release. 
1. Push the images to docker unofficial repo









