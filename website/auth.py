from . import db

from flask import render_template, Blueprint, request, flash, redirect, url_for

from .models import User

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_user, login_required, logout_user, current_user



auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return render_template('home.html', user=current_user)

@auth.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz1():
    if request.method=="POST":
        r1 = request.form.get('question1')
        r2 = request.form.get('question2')
        r3 = request.form.get('question3')
        r4 = request.form.get('question4')
        r5 = request.form.get('question5')
        points = 0
        if r1 == "A computer on a blockchain network":
            points += 10
        else:
            points -= 5
        if r2 == "Public and Private keys":
            points += 10
        else:
            points -= 5
        if r3 == "Peer to Peer":
            points += 10
        else:
            points -= 5
        if r4 == "Satoshi Nakamoto":
            points += 10
        else:
            points -= 5
        if r5=="Computers that validate and process blockchain transactions":
            points+=10
        else:
            points-=5        
        flash(f'Total points:-{points}', category="success")
    return render_template('quiz.html', user=current_user)
@auth.route('/quiz2', methods=['GET', 'POST'])
@login_required
def quiz2():
    if request.method=="POST":
        r1 = request.form.get('2question1')
        r2 = request.form.get('2question2')
        r3 = request.form.get('2question3')
        r4 = request.form.get('2question4')
        r5 = request.form.get('2question5')
        points = 0
        if r1 == "Use of capital on assets to receive returns":
            points += 10
        else:
            points -= 5
        if r2 == "All features of obtaining and using financial resources for company operations":
            points += 10
        else:
            points -= 5
        if r3 == "Worksheet":
            points += 10
        else:
            points -= 5
        if r4 == "Worksheet":
            points += 10
        else:
            points -= 5
        if r5=="None of the above":
            points+=10
        else:
            points-=5        
        flash(f'Total points:-{points}')
    return render_template('quiz2.html', user=current_user)

@auth.route('/quiz3', methods=['GET', 'POST'])
@login_required
def quiz3():
    if request.method=="POST":
        r1 = request.form.get('question1')
        r2 = request.form.get('question2')
        r3 = request.form.get('question3')
        r4 = request.form.get('question4')
        r5 = request.form.get('question5')
        points = 0
        if r1 == "Monetary policy":
            points += 10
        else:
            points -= 5
        if r2 == "Capital market":
            points += 10
        else:
            points -= 5
        if r3 == "All of the above":
            points += 10
        else:
            points -= 5
        if r4 == "SEBI":
            points += 10
        else:
            points -= 5
        if r5=="Profit":
            points+=10
        else:
            points-=5        
        flash(f'Total points:-{points}', category="success")
    return render_template('quiz3.html', user=current_user)
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('home.html', user=current_user)

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
            
    return render_template("login.html", user=current_user)

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
            
  
    return render_template('Signup.html',user=current_user)

@auth.route('/about-us')
def aboutus():
    return render_template('about_us.html', user=current_user) 

@auth.route('/learn')
@login_required
def learn():
    return render_template('learning.html', user=current_user)