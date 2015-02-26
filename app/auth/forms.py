from flask import flash 
from flask.ext.wtf import Form 
from wtforms import TextField, SubmitField, ValidationError, PasswordField, BooleanField, validators
from ..models import User
# from .. import db, login_manager 

def username_exist(form, field):
    l = User.query.filter_by(username=form.username.data).all()
    print l
    if len(l) != 0:
        raise ValidationError("Username already exists. Try something else.")

def username_dne(form, field):
    l = User.query.filter_by(username=form.username.data).all()
    if len(l) == 0:
        raise ValidationError("Username does not exist. Try again.")

def password_wrong(form, field):
    user = User.query.filter_by(username=form.username.data).first()
    if user == None:
        raise ValidationError("Incorrect password and username combination")
    if not user.check_password(form.password.data):
        raise ValidationError("Incorrect password and username combination")

class LoginForm(Form):
    username = TextField("Username", [validators.DataRequired(), username_dne])
    password = PasswordField("Password", [validators.DataRequired(), password_wrong])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign in")

class RegisterForm(Form):
    username = TextField("Username", [validators.Length(5,25), username_exist])
    password = PasswordField("Password",[validators.length(7, 25), validators.EqualTo('retype_password', message = "Passwords must match")])
    retype_password = PasswordField("Retype Password", [validators.DataRequired()])
    submit = SubmitField("Create Account")

        


