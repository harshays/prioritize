import os 
from flask.ext.script import Manager
from app import db, create_app 

app = create_app('default')
manager = Manager(app)

if __name__ == "__main__":
    manager.run()

