from flask import render_template, request, redirect, url_for
from application.model import SQLDatabase
from application.log_manager import EmailLogManager
from flask_mail import *
from flask_login import LoginManager, login_user, login_required, logout_user
from application.forms import LoginForm
from application import app
import logging, json, xmltodict
from datetime import date
from application.user import User


# Email Management
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'cienfuegosjdevelop@gmail.com',
    MAIL_PASSWORD = 'Promagic1'
    )
mail = Mail(app)
emailmanager = EmailLogManager()
elogger = emailmanager.getEmailLogger()


# Login Management Objects
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login = "login"

# Database Connection
conn_cred = None
with open('cred.xml') as fd:
    conn_cred = xmltodict.parse(fd.read())
database = SQLDatabase(conn_cred=conn_cred)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        # Verify Credentials
        q = "SELECT * FROM users WHERE email='{0}' AND password='{1}'".format(email, password)
        results = database.query(q)

        if results is not None and len(results) != 0:
            usr = User(results[0]['UID'], results[0]['email'], results[0]['password'])
            login_user(usr)
            return redirect(url_for("user_dashboard", user=results[0]['UID']))
        else:
            return render_template("login.html", title="Login | GameChain", active="home", loginFailed=True)

    else:
        q = "SELECT * FROM users"
        results = database.query(q)
        invalidEmails = []
        if results is not None:
            for user_info in results:
                invalidEmails.append(user_info['email'])

        return render_template("login.html", title="Login | GameChain", active="home", loginFailed=False, invalidEmails=invalidEmails)


@app.route("/create_account", methods=["POST"])
def create_account():

    email = request.form['reg_email']
    password = request.form['pwd']
    firstname = request.form['first_name']
    lastname = request.form['last_name']
    firm_name = request.form['firm_name']

    q = "INSERT INTO users(" \
        "password, first_name, last_name," \
        "email, account_confirmed, firm_name" \
        "VALUES ('{0}', '{1}', '{2}', " \
        "'{3}', '{4}');".format(
        password, firstname, lastname, email, firm_name
    )

    print(database.insert(q))

    bSent = False
    try:
        msg = Message("GameChain: E-mail Confirmation",
                      sender="cienfuegosjdevelop@gmail.com",
                      recipients=[email])
        msg.html = render_template("confirmation_email.html", firstname=firstname)
        mail.send(msg)
        bSent = True
    except Exception as e:
        elogger.log(logging.INFO, "{0} Could not send confirmation e-mail to {1}.".format(date.today(), email))
        bSent = False
    finally:
        if bSent:
            elogger.log(logging.INFO, "{0}. Confirmation e-mail sent to {1}.".format(date.today(), email))

    return redirect(url_for('email_confirmation', successful=bSent))


@app.route("/email_confirmation/<successful>", methods=["GET"])
def email_confirmation(successful):
    return render_template("email_confirmation.html", successful=successful)


@login_manager.user_loader
def load_user(userid):
    q = "SELECT * FROM user_account_info WHERE UID='{0}'".format(userid)
    results = database.query(q)
    if results is not None:
        return User(userid, results[0]['email'], results[0]['password'])
    else:
        return None


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.errorhandler(401)
def page_not_found(e):
    return redirect(url_for('login'))


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="About | Organizer")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", title="Contact | Organizer")
    else:
        # Do any email contact things here
        pass