from flask import Flask, jsonify
from flask_cors import CORS
import time

# configuration
DEBUG = True

# Init flask
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify("pong !!! Secondes : " + str(int(time.time())))

@app.route('/welcome', methods=['GET'])
def welcome_message():
    
    return jsonify({"main_title" : "Bienvenue sur photobooth 2.0", "sub_title": "Appuyer sur le bouton bleu pour démarrer"})

if __name__ == '__main__':
    app.run("0.0.0.0")
