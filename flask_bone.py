"""

This file has a simple Flask "server" App for configuring, reading and setting BeagleBone IO over HTTP.

Requirements:

1.  virtualenv - $ sudo pip install virtualenv

Install instructions:

1.  $ git clone
2.  $ cd flask_bone.py
3.  $ virtualenv venv
4.  $ . venv/bin/activate
5.  $ pip install flask
6.  $ pip install Adafruit_BBIO

Run instructions:

1.  $ export FLASK_APP=flask_bone.py
2.  $ flask run --host=0.0.0.0 // This will expose your app to the world wide web

To run on boot, create a cron job:

1. $ sudo crontab -e

    Select an editor and add the line:

    @reboot cd /path/to/flask_bone && . venv/bin/activate && export FLASK_APP=flask_bone.py && flask run --host=0.0.0.0 &

    to the bottom of the file.

    This will start the server on reboot.

"""

import Adafruit_BBIO.GPIO as GPIO
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'You have reached the Beagle Bone IO server.'


@app.route('/input/config/<gpio>')
def config_input(gpio):
    try:
        GPIO.setup(gpio, GPIO.IN)
        return 'Successfully configured {} as input.'.format(gpio)
    except Exception as e:
        return e


@app.route('/input/get/<gpio>')
def get_input(gpio):
    try:
        state = '{} state: {}'.format(gpio, GPIO.input(gpio))
        return state
    except Exception as e:
        return 'Error reading input, did you configure {} as an input?'.format(gpio), e    


@app.route('/output/config/<gpio>')
def config_output(gpio):
    try:
        GPIO.setup(gpio, GPIO.OUT)
        return 'Successfully configured {} as output.'.format(gpio)
    except Exception as e:
        return e


@app.route('/output/set_high/<gpio>')
def set_output_high(gpio):
    try:
        GPIO.output(gpio, GPIO.HIGH)
        return 'Successfully set {} output high.'.format(gpio)
    except Exception as e:
        return 'Error setting output, did you configure {} as an output?'.format(gpio), e


@app.route('/output/set_low/<gpio>')
def set_output_low(gpio):
    try:
        GPIO.output(gpio, GPIO.LOW)
        return 'Successfully set {} output low.'.format(gpio)
    except Exception as e:
        return 'Error setting output, did you configure {} as an output?'.format(gpio), e
