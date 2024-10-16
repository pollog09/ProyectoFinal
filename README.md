# Diabeto

![Diabeto Banner](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/7304a882-5280-4444-9156-b330524036c6/d60uxie-5cd0ab54-acce-4454-818f-b6b05dc0e12f.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzczMDRhODgyLTUyODAtNDQ0NC05MTU2LWIzMzA1MjQwMzZjNlwvZDYwdXhpZS01Y2QwYWI1NC1hY2NlLTQ0NTQtODE4Zi1iNmIwNWRjMGUxMmYuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.YwRvA-feO5GcHeVtp8FAF3ECswTyouAREnVh8Pop3EI)

## Overview

Diabeto is a web application designed to predict diabetes in individuals using a machine learning model. The application is built using Python Flask for the backend and provides a user authentication system to access the model through a web UI.

## Project Structure

- `app/`: Contains the Flask application.
  - `__init__.py`: Initializes the Flask app and its extensions.
  - `routes.py`: Defines the routes for the web application.
  - `models.py`: Contains the database models.
  - `forms.py`: Defines the forms for user registration and login.
  - `templates/`: Contains the HTML templates.
  - `static/`: Contains static files like CSS and images.
- `config.py`: Configuration file for the application.
- `auth.py`: Handles authentication using Firebase.
- `model/`: Contains the machine learning model for diabetes prediction.

## Setup Instructions

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/diabeto.git
   cd diabeto
   ```

2. **Create a virtual environment and install dependencies**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Running the Project**
Run the Flask app:

Access the web application: Open your web browser and go to http://127.0.0.1:5000.

4. **Usage**
Register: Create a new user account.
Login: Access the web UI using your credentials.
Predict Diabetes: Use the machine learning model to predict diabetes based on user input.
