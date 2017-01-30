# flask-bone
Flask app to configure, read and write Beagle Bone IO

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
    
Example usage:

Configure GPIO0_26 as an input through your browser:

http://beagel_bone_ip:5000/input/config/GPIO0_26

Get the value of GPIO0_26:

http://beagle_bone_ip:5000/input/get/GPIO0_26
