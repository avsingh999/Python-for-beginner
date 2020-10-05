#Importing flask
from flask import Flask, render_template

app = Flask(__name__)

#URL to be specified 

#http://127.0.0.1:5000/
@app.route('/')
def hello_world():
    return 'Hello, World!'

#http://127.0.0.1:5000/about
@app.route('/about')
def about_flask():
    return render_template('aboutFlask.html')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()