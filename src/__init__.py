## Imports
import logging
from flask import Flask, render_template, request, redirect, url_for, flash, session
from src.providers import firebase, model

## App
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


## Routes
@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

## Registro Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        logger.info(f'Login attempt with username: {username}')
        if (firebase.login(username,password)==True):
            logger.info('Login successful')
            session['username'] = username  # Store username in session
            return redirect(url_for('dashboard'))
        else:
            logger.warning('Invalid login credentials')
            flash('Invalid login credentials', 'error')
            return redirect(url_for('login')) 
    else:
        logger.info('login page accessed')
        return render_template('login.html')
    
## Registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        signup = firebase.signup(username, password).args[1]
        logger.error(signup)
        if 'error' not in signup:
            logger.info('Registration successful')
            return redirect(url_for('login'))
        else:
            logger.warning('Registration failed')
            flash('Registration failed, username already exist or password complexity is below the required level', 'error')
            return redirect(url_for('register')) 
    else:
        logger.info('Register page accessed')
        return render_template('register.html')


## Dashboard
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    outcome = None
    if 'username' in session:
        if request.method == 'POST':
            try:
                Pregnancies = float(request.form['Pregnancies'])
                Glucose = float(request.form['Glucose'])
                BloodPressure = float(request.form['BloodPressure'])
                SkinThickness = float(request.form['SkinThickness'])
                Insulin = float(request.form['Insulin'])
                BMI = float(request.form['BMI'])
                DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
                Age = float(request.form['Age'])
                
                logger.info(f'Received form data: {request.form}')
                logger.info('===========================')
                outcome = model.run_model(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
                logger.info(f'Model outcome: {outcome}')
            except Exception as e:
                logger.error(f'Error processing form data: {e}')
        
        logger.info('Dashboard page accessed')
        return render_template('dashboard.html', outcome=outcome)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    logger.info('Logout action initiated')
    session.pop('username', None)  # Remove username from session
    return redirect(url_for('login'))