## Imports
import logging
from flask import Flask, render_template, request, redirect, url_for
from src.providers import firebase

## App
app = Flask(__name__)
# Logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


## Routes
@app.route('/')
def home():
    logger.info('Home page accessed')
    return render_template('login.html')

## Registro Login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    logger.info(f'Login attempt with username: {username}')

    if (firebase.login(username,password)==True):
        logger.info('Login successful')
        return redirect(url_for('dashboard'))
    else:
        logger.warning('Invalid login credentials')
        return redirect(url_for('home')) 
        
## Registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']        
        logger.error(firebase.signup(username, password))
        # Add your registration logic here
        if (firebase.signup(username, password)):
            logger.info('Registration successful')
            return redirect(url_for('login'))
        else:
            logger.warning('Registration failed')
            return 'Registration failed'
    else:
        logger.info('Register page accessed')
        return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    logger.info('Dashboard page accessed')
    return render_template('home.html')

@app.route('/logout')
def logout():
    logger.info('Logout action initiated')
    return redirect(url_for('home'))