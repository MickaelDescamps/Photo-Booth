from os import path
import sys
from crypt import methods
from http.client import HTTPResponse
import json
import time
import traceback
from flask import Flask, Response, jsonify, request, send_from_directory
from flask_cors import CORS
import time
import paho.mqtt.client as mqtt

# configuration
DEBUG = True
MESSAGE_BUTTON = []
MESSAGE_GOPRO = []
STATE = "WAIT"
NEW_PHOTO = ""
CLIENT_MQTT = None


# Init flask
app = Flask(__name__)
app.config.from_object(__name__)


base_path = path.dirname(path.abspath(__file__))

print(str(base_path))

config_file = f"{base_path!s}/configs.json"

print(config_file)

CONFIG = None

api_cors_config = {
    "origins": [
        "http://localhost:5000",
        "http://localhost:80"
    ],
    "methods": ["OPTIONS", "GET", "POST"],
    "allow_headers": ["Authorization"]
}

def load_confs():
    """Function to load app configs
    """

    try:
        global CONFIG
        
        with open(config_file, 'r') as file:
            CONFIG = json.loads(file.read())

            print(CONFIG)
    except BaseException as ex:
        print(repr(ex) + traceback.format_exc())
        
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
        "/opt/photo_booth/images", name
    )
@app.route('/api/get_state',methods=['GET'])
def get_state():

    try:

        global MESSAGE_BUTTON, MESSAGE_GOPRO, NEW_PHOTO, STATE, CLIENT_MQTT

        if len(MESSAGE_BUTTON) > 0:
            
            if STATE == "WAIT":
                CLIENT_MQTT.publish("gopro/take_picture", json.dumps({"time":time.time()}), qos=2, retain=False)
                STATE = "TAKE_PICTURE"
                MESSAGE_BUTTON = []
                ret = {"state": STATE}

            elif STATE == "REVIEW":
                STATE = "WAIT"
                MESSAGE_BUTTON = []
                ret = {"state": STATE}

        elif len(MESSAGE_GOPRO) > 0:
            if STATE == "TAKE_PICTURE":
                STATE = "REVIEW"
                NEW_PHOTO = MESSAGE_GOPRO[-1]["photo_name"]
                ret = {"state": STATE, "photo_name" : NEW_PHOTO}
                MESSAGE_GOPRO = []

        else:
            ret = {"state": STATE}

            if STATE == "REVIEW":
                ret["photo_name"] = NEW_PHOTO

        return Response(json.dumps(ret), status=200)

    except BaseException as ex:
        print(MESSAGE_BUTTON)
        print(MESSAGE_GOPRO)
        print(STATE)
        print(repr(ex) + traceback.format_exc())
        ret = {}

        return Response(json.dumps(ret), status=200)


def on_message(client, userdata, message):

    global MESSAGE_BUTTON, MESSAGE_GOPRO

    if message.topic == "button/all":

        new_message_content = message.payload.decode("utf-8")
        new_message_time = json.loads(new_message_content)

        if len(MESSAGE_BUTTON) == 0:
            MESSAGE_BUTTON.append(new_message_time["time"])
            print(f"Message cas 1 : {new_message_time['time']!s}")

        elif new_message_time["time"] - MESSAGE_BUTTON[-1] > 0.25:
            MESSAGE_BUTTON.append(new_message_time["time"])
            print(f"Message cas 2 : {new_message_time['time']!s}")

        print(MESSAGE_BUTTON)

    elif message.topic == "gopro/new_image":

        gopro_message = json.loads(message.payload.decode("utf-8"))

        if len(MESSAGE_GOPRO) == 0:
            MESSAGE_GOPRO.append(gopro_message)
        
        elif gopro_message["time"] - MESSAGE_GOPRO[-1]["time"] > 0.25:
            MESSAGE_GOPRO.append(gopro_message)

    

if __name__ == '__main__':
    try:

        load_confs()

        CLIENT_MQTT = mqtt.Client()
        CLIENT_MQTT.connect("localhost", port=1883)
        CLIENT_MQTT.subscribe("button/#",2)
        CLIENT_MQTT.subscribe("gopro/new_image",2)
        CLIENT_MQTT.on_message = on_message
        CLIENT_MQTT.loop_start()

        app.run("0.0.0.0")

        CLIENT_MQTT.loop_stop()
    except BaseException as ex:
        save_confs()
        print(str(ex))
