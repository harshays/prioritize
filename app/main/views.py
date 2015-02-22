from flask import redirect, render_template, flash, g, session 
from . import main
# from .forms import LoginForm, RegisterForm, TodoForm
from .. import db 
# from ../models import User, Todo

@main.app_errorhandler(404)
def page_not_found(e):
    return "Implement common error page", 404 

@main.app_errorhandler(500)
def page_not_found(e):
    return "Implement common error page", 500 

@main.route('/',methods=["GET","POST"])
def index():
    return render_template("index.html")
