from flask import render_template
from forms import LoginForm
from application import app


@app.route("/")
def index():
    return render_template("index.html",
                            title="Home")
                            
                            
@app.route("/login", methods = ["GET", "POST"])                            
def login():
    form = LoginForm()
    return render_template("login.html",
                            title = "Sign In"
                            form = form)