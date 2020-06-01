from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True   # enable debug mode for development

@app.route('/')
def hello_world():
    return 'Hello to the World of Flask!'


if __name__ == '__main__':
    app.run()