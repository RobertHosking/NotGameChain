#!/usr/bin/python
import sys
sys.path.insert(0, "/var/www/PAYVR/app/application")


from application import app

if __name__ == "__main__":
    app.run()

