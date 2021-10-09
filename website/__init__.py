from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "userinfo.db"

def create_database(app):

    if not path.exists("website/" + DB_NAME):
        try:
            db.create_all(app=app)
            print("Database Loaded Successfully...")
        except Exception as e:
            print(e)

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DB_URI'] = f"sqllite:///{DB_NAME}"
    app.config['SECRET_KEY'] = 'eCoN@#$HaCks@@#BanGALore'
    db.init_app(app)

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User
    create_database(app)

    return app
