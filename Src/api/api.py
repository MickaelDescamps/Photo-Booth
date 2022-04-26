""" Python API for photo booth website

Required: Flask, Python 3.8+

Author: Mickaël Descamps - <mickael.descamps@mineyou.fr> - @MickaelDescamps (github)

Created: 24 April, 2022

"""

# imports
from flask import Flask, jsonify
from flask_cors import CORS

# Configuration
DEBUG = True

# Init flask
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, ressources={r'/*': {'origins': '*'}})


@app.route('/')
def index():
    return "Hello world !!!"

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify("pong !")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
