import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"]= os.getenv("DATABASE_URI") 
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
    app.config['JSON_SORT_KEYS'] = True


    db.init_app(app)

    from app.models.user_model import User

    app.db= db

    import app.models
     


    