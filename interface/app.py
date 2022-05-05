from crypt import methods
from http.client import HTTPResponse
import json
from lib2to3.pytree import Base
import time
import traceback
from flask import Flask, Response, jsonify, request, send_from_directory
from flask_cors import CORS
import time

# configuration
DEBUG = True


# Init flask
app = Flask(__name__)
app.config.from_object(__name__)

config_file = "/root/Photo-Booth/interface/configs.json"

CONFIG = None

api_cors_config = {
    "origins": [
        "http://localhost:5000",
        "http://localhost:8080"
    ],
    "methods": ["OPTIONS", "GET", "POST"],
    "allow_headers": ["Authorization"]
}

def load_confs():
    """Function to load app configs
    """
    global CONFIG
    
    with open(config_file, 'r') as file:
        CONFIG = json.loads(file.read())        
        
def save_confs():
    """Function to save app configs
    """
    
    with open(config_file, 'w') as file:
        file.write(json.dumps(CONFIG))
    

CORS(app, ressources = {"/*": api_cors_config})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify("pong !!! Secondes : " + str(int(time.time())))

@app.route('/welcome', methods=['GET'])
def welcome_message():
    
    return jsonify(CONFIG["welcome"])

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
    CONFIG = data["config"]
    save_confs()
    return Response("true",status=200)

@app.route('/api/count', methods=['GET'])
def get_take_photo_count():
    
    count = 10 - int(time.time() % 10)
    
    response = {"count": count}
    response = json.dumps(response)
    
    return Response(response, status=200)    

@app.route("/photos/<path:name>")
def get_file(name):
    return send_from_directory(
        "/root/Photo-Booth/photos", name
    )
    

if __name__ == '__main__':
    try:
        load_confs()
        app.run("0.0.0.0")
    except BaseException as ex:
        save_confs()
        print(str(ex))
