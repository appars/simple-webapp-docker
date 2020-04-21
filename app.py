import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Sivas: Welcome to simple OpenShift Demo!!!!"

@app.route('/howareyou')
def hello():
    return 'I am good, Thanks. How about you?'

if __name__ == "__main__":
    app.run()
