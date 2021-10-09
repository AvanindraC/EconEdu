from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
'''
db = SQLAlchemy()
DB_NAME = "userinfo.db"

def create_database(app):

    if not path.exists("website/" + DB_NAME):
        try:
            db.create_all(app=app)
            print("Database Created Successfully...")
        except Exception as e:
            print(e)

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DB_URI'] = f"sqllite:///{DB_NAME}"
    db.init_app(app)

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User
    create_database(app)

    return app
'''
def create_app():


    app = Flask(__name__)
	 
    @app.route('/')

    def home():
        return render_template('home.html')
	 
    @app.route('/login')
    def login():
        return render_template('login.html')
    return app
    