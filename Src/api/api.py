""" Python API for photo booth website

Required: Flask, Python 3.8+

Author: Mickaël Descamps - <mickael.descamps@mineyou.fr> - @MickaelDescamps (github)

Created: 24 April, 2022

"""

# imports
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !!!"

app.run(host="0.0.0.0")
