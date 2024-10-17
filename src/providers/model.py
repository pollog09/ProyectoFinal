import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import load_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
    

def run_model(Glucose,BloodPressure,SkinThickness,Insulin,BMI):
    modelo = keras.models.load_model("model/diabetes_model.h5")
    try:
        result = modelo.predict(Glucose,BloodPressure,SkinThickness,Insulin,BMI)
        print(result)
    except Exception as e:
        print(f"========================================\r\nAn error occurred: {e}\r\n========================================")
    return