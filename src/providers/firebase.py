import pyrebase
from src.providers import config

firebaseConfig=config.firebaseConfig
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

def login(email,password):
    try:
        login = auth.sign_in_with_email_and_password(email,password)
    except:
        print ("Invalid email or password")
    

def signup(email, password):
    try:
        user= auth.create_user_with_email_and_password(email,password)
    except Exception as e:
        print(e)
    return

