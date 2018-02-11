from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import Datarequired




class LoginForm(Form):
    username = Stringfield('username', validators=[Datarequired()])
    password = Passwordfield('password', validators=[Datarequired()])