#!/usr/bin/python
#import random
import base64
import os
import sys
import logging

activate_this = '/var/www/mostplayed/mp/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)

BASE_DIR = os.path.join(os.path.dirname(__file__)) #gets this current location
if BASE_DIR not in sys.path:
    sys.path.insert(0,BASE_DIR)

from mp import app as application

####set in __init__.py
#application.secret_key = str(base64.b64encode(os.urandom(24))) #application.secret_key = 'this is a random string'


