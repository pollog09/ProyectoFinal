import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import load_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
    

def run_model(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    modelo = keras.models.load_model("model/diabetes_model.h5")
    try:
        result = modelo.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
    return