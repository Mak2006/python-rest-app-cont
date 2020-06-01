from flask import Flask
from flask import render_template

# Create the Flask application instance
app = Flask(__name__, template_folder="static")



#Load configuration from configuration.py
# this loads the debug values and secret keys etc.
# handles different environments.
app.config.from_object('configuration.DevelopmentConfig');



# We create a landing page
@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()