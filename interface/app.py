from crypt import methods
from http.client import HTTPResponse
import json
import traceback
from flask import Flask, Response, jsonify, request
from flask_cors import CORS
import time

# configuration
DEBUG = True
CONFIG = {}

CONFIG["main_title"] =  "Bienvenue sur photobooth 2.0"
CONFIG["sub_title"] = "Appuyer sur le bouton bleu pour demarrer"


# Init flask
app = Flask(__name__)
app.config.from_object(__name__)

api_cors_config = {
    "origins": [
        "http://localhost:5000",
        "http://localhost:8080"
    ],
    "methods": ["OPTIONS", "GET", "POST"],
    "allow_headers": ["Authorization"]
}

CORS(app, ressources = {"/*": api_cors_config})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify("pong !!! Secondes : " + str(int(time.time())))

@app.route('/welcome', methods=['GET'])
def welcome_message():
    
    return jsonify(CONFIG)

@app.route('/config', methods=['GET'])
def get_config():
    try:
    
        return jsonify(CONFIG)
    
    except BaseException as ex:
        print(repr(ex) + " - " + traceback.format_exc())

@app.route('/config', methods=['POST', 'OPTIONS'])
def set_config():
    global CONFIG
    
    data = json.loads(request.data)
    print(str(data))
    CONFIG['main_title'] = data["main_title"]
    CONFIG['sub_title'] = data["sub_title"]
    
    return Response("true",status=200)

if __name__ == '__main__':
    app.run("0.0.0.0")
