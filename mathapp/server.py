from flask import Flask
from flask import render_template, jsonify, request


from mathapp.service import sum

import logging.handlers
from logging import Formatter, FileHandler

# Create the Flask application instance
app = Flask(__name__, template_folder="static")

RESULT = "The result of the addition is {}."

# Load configuration from configuration.py
# this loads the debug values and secret keys etc.
# handles different environments.
app.config.from_object('configuration.DevelopmentConfig');


# We create a landing pagem, the ui  part, @todo microservice
@app.route('/')
def home():
    app.logger.info('Rendering home ')
    return render_template('home.html')


# the server part, @todo microservice
# It is exposed as as POST method using `@mathapp.route('/mathapp/api/v1.0/add', methods=['POST'])`. The input parameters are obtained via `a = request.json.get('number1', 0);` where `number1` matches the input field. The data is then converted to floats. Then the result is then returned via jsonify object
@app.route('/mathapp/api/v1.0/add', methods=['POST'])
def add():
    app.logger.info('Call to add api ')

    # Making sure we inform the use if any other content type is being sent
    content_type = request.headers['Content-Type']
    app.logger.info('content type ' + str(content_type))
    if (content_type != "application/x-www-form-urlencoded"):
        raise Exception("content type {} is not supported by mathapp".format(content_type))

    # Obtain the inputs
    a = request.values.get('number1')
    b = request.values.get('number2')
    c = request.values.get('number3')
    msg = "Input values obtained are a={}, b={} c={}".format(a, b, c)
    app.logger.info(msg)

    # converting to int
    #data = [float(a), float(b), float(c)]
    data = [a, b, c]

    #for the result
    result = RESULT.format(sum(data))

    # return

    return render_template('home.html', Result=result )

# Add a 404 custom for pytest
@app.errorhandler(404)
def key_error(e):
    app.logger.error('404 encountered -' + request.path)
    return render_template('404.html'), 404

#Add a custom 500 for pytest
@app.errorhandler(Exception)
def internal_server_error(e):
    return render_template("500.html", error = str(e))



#Make it run.
if __name__ == '__main__':
    handler = FileHandler('C:\log\mathapp.log')
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(filename)s:%(lineno)d]'
    ))
    app.logger.addHandler(handler)
    app.logger.info("*** App started ")
    app.logger.info('Log test info')


    app.run()