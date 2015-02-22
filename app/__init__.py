from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config 

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    
    # set up app config
    app.config.from_object(config[config_name])

    # init app from config class static function
    config[config_name].init_app(app)

    db.init_app(app)

    # blueprint routes and handlers init
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app 
