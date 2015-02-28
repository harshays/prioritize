from flask import flash 
from flask.ext.wtf import Form 
from wtforms import TextField, SubmitField, ValidationError, PasswordField, BooleanField, validators
# from ..models import User, 

class TodoForm(Form):
    todo = TextField("", [validators.DataRequired()])
    submit = SubmitField("Add task")
