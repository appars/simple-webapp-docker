import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to Simple Webapp Docker demo with OpenShift!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run()
