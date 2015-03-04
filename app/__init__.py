from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_bootstrap import Bootstrap
from config import config 

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()

login_manager.session_protection = "basic"
login_manager.login_view = "auth.login"


def create_app(config_name):
    app = Flask(__name__)
    
    # set up app config
    app.config.from_object(config[config_name])
    app.secret_key = app.config["SECRET_KEY"]

    # init app from config class static function
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    # blueprint routes and handlers init
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for auth
    from auth import auth as auth_blueprint 
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app
