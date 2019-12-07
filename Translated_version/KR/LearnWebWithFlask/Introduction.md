##FLASK FRAMEWORK
Flask is a Python-based web development framework built with a small core and easy-to-extend philosophy.

##WHY FLASK?
Flask is also easy to get started with as a beginner since it contains very less code to start with.
It allows the developer to run the website on the server with the DB connectivity as well.

##EXAMPLE CODE
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()


##RUN THE CODE
> python index.py

##DEFAULT PORT
Default port for Flask is 5000

##TEMPLATES
HTML pages are always added in the Templates folder.