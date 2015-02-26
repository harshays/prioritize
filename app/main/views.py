from flask import redirect, render_template, flash, g, session, url_for, request
from flask.ext.login import current_user, login_required
from . import main
from .forms import TodoForm
from .. import db 
from ..models import User

@main.app_errorhandler(404)
def page_not_found(e):
    return redirect(url_for('main.index'))

@main.app_errorhandler(500)
def page_not_found(e):
    return redirect(url_for('main.index'))

@main.route('/',methods=["GET","POST"])
def index():
    if current_user.is_authenticated():
        url = url_for('main.profile')
        return redirect(url)
    return render_template("index.html")

@main.route('/profile',methods=["GET","POST"])
@login_required
def profile():
    form = TodoForm()

    if request.method == "GET":
        return render_template("profile.html", form = form)
    elif request.method == "POST" and form.validate_on_submit():
        return render_template("profile.html", form = form)
