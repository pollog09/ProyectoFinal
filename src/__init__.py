## Imports
import logging
from flask import Flask, render_template, request, redirect, url_for
from src.providers import firebase, model

## App
app = Flask(__name__)
# Logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


## Routes
@app.route('/')
def home():
    return redirect(url_for('home'))

## Registro Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        logger.info(f'Login attempt with username: {username}')
        if (firebase.login(username,password)==True):
            logger.info('Login successful')
            return redirect(url_for('dashboard'))
        else:
            logger.warning('Invalid login credentials')
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
        logger.error(firebase.signup(username, password))
        if (firebase.signup(username, password)):
            logger.info('Registration successful')
            return redirect(url_for('login'))
        else:
            logger.warning('Registration failed')
            return 'Registration failed'
    else:
        logger.info('Register page accessed')
        return render_template('register.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    outcome = None
    if request.method == 'POST':
        Pregnancies = int(request.form['Pregnancies'])
        Glucose = int(request.form['Glucose'])
        BloodPressure = int(request.form['BloodPressure'])
        SkinThickness = int(request.form['SkinThickness'])
        Insulin = int(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = int(request.form['Age'])
        
        outcome = model.run_model(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI)
    
    logger.info('Dashboard page accessed')
    return render_template('dashboard.html', outcome=outcome)

@app.route('/logout')
def logout():
    logger.info('Logout action initiated')
    return redirect(url_for('home'))