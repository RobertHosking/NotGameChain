from flask import render_template
from model import SQLDatabase
from log_manager import EmailLogManager

from application.forms import LoginForm
from application import app

                            
@app.route("/", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html",
                            title = "Sign In")
