# Diabeto

![Diabeto Banner](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/7304a882-5280-4444-9156-b330524036c6/d60uxie-5cd0ab54-acce-4454-818f-b6b05dc0e12f.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzczMDRhODgyLTUyODAtNDQ0NC05MTU2LWIzMzA1MjQwMzZjNlwvZDYwdXhpZS01Y2QwYWI1NC1hY2NlLTQ0NTQtODE4Zi1iNmIwNWRjMGUxMmYuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.YwRvA-feO5GcHeVtp8FAF3ECswTyouAREnVh8Pop3EI)

## Overview

Diabeto is a web application designed to predict diabetes in individuals using a machine learning model. The application is built using Python Flask for the backend and provides a user authentication system to access the model through a web UI.

## Project Structure

```
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── providers/
│   │   ├── firebase.py
│   │   ├── model.py
│   │   └── __init__.py
│   ├── static/
│   │   ├── styles.css
│   │   └── dashboard.css
│   └── templates/
│       ├── login.html
│       ├── register.html
│       └── dashboard.html
├── .gitignore
├── requirements.txt
└── README.md
```


## Setup Instructions

### Prerequisites

- Python 3.12
- Virtual environment (optional but recommended)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/your_project.git
    cd your_project
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up Firebase configuration:**
    - Create a `config.py` file in the `src/providers/` directory with your Firebase configuration:
    ```python
    firebaseConfig = {
        "apiKey": "YOUR_API_KEY",
        "authDomain": "YOUR_AUTH_DOMAIN",
        "databaseURL": "YOUR_DATABASE_URL",
        "projectId": "YOUR_PROJECT_ID",
        "storageBucket": "YOUR_STORAGE_BUCKET",
        "messagingSenderId": "YOUR_MESSAGING_SENDER_ID",
        "appId": "YOUR_APP_ID"
    }
    ```

5. **Run the application:**
    ```sh
    flask run
    ```

## Usage

1. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:5000/`.

2. **Login or Register:**
    - Use the login page to log in with your credentials.
    - If you don't have an account, use the register page to create one.

3. **Dashboard:**
    - After logging in, you will be redirected to the dashboard.
    - Fill in the form with the required fields:
        - Pregnancies
        - Glucose
        - Blood Pressure
        - Skin Thickness
        - Insulin
        - BMI
        - Diabetes Pedigree Function
        - Age
    - Click the "Submit" button to get the diabetes probability.

## Project Details

- **Backend:** Flask
- **Frontend:** HTML, CSS
- **Machine Learning Model:** TensorFlow/Keras
- **Authentication:** Firebase
