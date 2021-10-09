from flask import render_template, Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/')
def home():
    return render_template('home.html')

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/sign-up')
def signup():
    return render_template('Signup.html')

@auth.route('/about-us')
def aboutus():
    return render_template('about_us.html')