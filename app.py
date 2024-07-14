from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello, Abdul Salam! how are you i am fine'

from controllers import product_controller, user_controller




