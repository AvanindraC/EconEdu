from . import db

from flask import render_template, Blueprint, request, flash, redirect, url_for

from .models import User

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return render_template('home.html')

@auth.route('/quiz')
def quiz():
    return render_template('quiz.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('/')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=="POST":
        email = request.form.get('email')
        pwd = request.form.get('pwd')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, pwd):
                flash('Logged in successfully', category="success")
                login_user(user, remember="True")
                return redirect(url_for('auth.home'))
            else:
                flash('Incorrect Password, please try again', category="error")
        else:
            flash("User doesn't exist. Please sign Up", category="error")
            
    return render_template("login.html") # do we need this one eh?

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    
    if request.method=="POST":
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('pwd') # type => str
        password2 = request.form.get('cpwd') # type => str
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 5:
            flash('E-mail must be larger than 4 characters', category="error")
        elif password1 != password2:
                flash("Passwords don't match", category="error")
        elif len(password1) < 8:
            flash('Passwords should be atleast 8 ', category="error")
        elif len(name) < 2:
            flash('Name must be atleast 2 characters long', category="error")
        else:
            new_user = User(
                email=email, 
                first_name=name, 
                password=generate_password_hash(password1, method="sha256"
                ))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Successfully created!', category="success")
            
  
    return render_template('Signup.html')

@auth.route('/about-us')
def aboutus():
    return render_template('about_us.html') 