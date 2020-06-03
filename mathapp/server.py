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
    """Method is the endpoint for root of the application.

    This takes no argument and returns the homepage of the application.

    Args:
        None

    Returns:
        home.html
    """
    app.logger.info('Rendering home ')
    return render_template('home.html')


# the server part, @todo microservice
# It is exposed as as POST method using `@mathapp.route('/mathapp/api/v1.0/add', methods=['POST'])`. The input parameters are obtained via `a = request.json.get('number1', 0);` where `number1` matches the input field. The data is then converted to floats. Then the result is then returned via jsonify object
@app.route('/mathapp/api/v1.0/add', methods=['POST'])
def add():
    """Method to service the add endpoint.

    This method retrieves the parameters from POST request.
    It sepecifically looks for the `number1` `number2` and `number3` as the keys.
    It then calls the `service.py` which computes the addition.
    Finally it redirects to `home.html` with the result set.

    Args:
        number1 : int - first number, parameter taken from the POST payload
        number2 : int - second number,  parameter taken from the POST payload
        number3 : int - third number,  parameter taken from the POST payload
    Returns:
        int: result of addition of all the elements within arg.
    	str: reason why it could not perform addition.
    """
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
    res = sum(data)

    result = RESULT.format(res)
    if type(res) == int:
        result = RESULT.format(res)
    else:
        app.logger.error('Sum returned error' + res)
        result = res # sum returned an error

    # return
    return render_template('home.html', Result=result )

# Add a 404 custom for pytest
@app.errorhandler(404)
def key_error(e):
    """Handler for 404 error

    It logs the error and redirects to 404.html
    Args:
        e : Exception
    Returns:
        404.html
    """
    app.logger.error('404 encountered -' + request.path)
    return render_template('404.html'), 404

#Add a custom 500 for pytest
@app.errorhandler(Exception)
def internal_server_error(e):
    """Handler for 500 error

    It logs the error and redirects to 500.html with the `error` parameter populated
    Args:
        e : Exception
    Returns:
        500.html
    """
    app.logger.error('500 encountered')
    return render_template("500.html", error = str(e))



#Make it run.
if __name__ == '__main__':
    """Main routine

    This initializes a Flask applicaiton. 
    It then creates a log file. The log file would be found in `C:/log/mathapp.log`
    Args:
        e : Exception
    Returns:
        500.html
    """

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