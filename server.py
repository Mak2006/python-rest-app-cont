from flask import Flask

app = Flask(__name__)

#Load configuration from configuration.py
# this loads the debug values and secret keys etc.
# handles different environments.
app.config.from_object('configuration.DevelopmentConfig')

@app.route('/')
def hello_world():
    return 'Hello to the World of Flask!'


if __name__ == '__main__':
    app.run()