import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import load_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
    

def run_model(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    modelo = keras.models.load_model("model/diabetes_model.h5")
    try:
        print("========================================Running Model========================================")
        input_data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        input_data = np.array(input_data, dtype=float)
        result = modelo.predict(input_data)
        print(result[0][0])
    except Exception as e:
        print(f"========================================\r\nAn error occurred: {e}\r\n========================================")
    return