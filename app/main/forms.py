from flask import flash 
from flask.ext.wtf import Form 
from wtforms import TextField, SubmitField, ValidationError, BooleanField, validators
from ..models import Todo 
import views
from flask.ext.login import current_user

def todo_exists(form, field):
    todo = views.parse_todo(form.todo.data)[0]
    print todo
    todo_db = current_user.todo.filter_by(description = todo).first()
    if todo_db != None:
        raise ValidationError("Task already exists")


class TodoForm(Form):
    todo = TextField("", [validators.DataRequired(), todo_exists])
    submit = SubmitField("Add task")
