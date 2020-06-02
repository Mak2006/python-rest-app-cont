from flask import Flask
from flask import render_template, jsonify, request

from app.value_object import Valueobj


# Create the Flask application instance
app = Flask(__name__, template_folder="static")




# Load configuration from configuration.py
# this loads the debug values and secret keys etc.
# handles different environments.
app.config.from_object('configuration.DevelopmentConfig');


# We create a landing pagem, the ui  part, @todo microservice
@app.route('/')
def home():
    return render_template('home.html')


# the server part, @todo microservice
# It is exposed as as POST method using `@app.route('/bigmaths/api/v1.0/add', methods=['POST'])`. The input parameters are obtained via `a = request.json.get('number1', 0);` where `number1` matches the input field. The data is then converted to floats. Then the result is then returned via jsonify object
@app.route('/bigmaths/api/v1.0/add', methods=['POST'])
def add():
    # Obtain the inputs
    a = request.json.get('number1', 0);
    b = request.json.get('number2', 0);
    c = request.json.get('number3', 0);

    # converting to int
    a, b, c = float(a), float(b), float(c)

    #create a value object
    vo = Valueobj(a, b, c)

    #for the result
    result = {
        'result': add(vo) # call the service with the vo.
    }

    # return
    return jsonify({'result': result}), 201

#this forms our actual data layer.
def add(vo):
    return vo.addservice()

#Make it run.
if __name__ == '__main__':
    app.run()