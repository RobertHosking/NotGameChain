import os
import sys

from application import app
sys.path.insert(0,'/home/ubuntu/workspace/')

# Builds the server configuration
if os.getenv('IP'):
  IP    = os.getenv('IP')
else:
  IP    = '0.0.0.0'

if os.getenv('PORT'):
  PORT  = int(os.getenv('PORT'))
else:
  PORT  = 8080


app.run(host = IP, port = PORT, debug = True, threaded = True)
