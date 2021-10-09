from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0',port=8080)