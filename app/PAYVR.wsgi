#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/PAYVR/")

from application import app as application
application.secret_key = 'supper-secret-stuff'
