#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.append('/var/')
sys.path.append("/var/www/")
sys.path.append("/var/www/PAYVR/")
sys.path.append("/var/www/PAYVR/application/")
from application import app

if __name__ == "__main__":
    app.run()

