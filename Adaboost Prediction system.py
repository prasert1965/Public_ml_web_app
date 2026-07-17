# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:20:43 2024

@author: Administrator
"""

import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# loading the saved model
loaded_model = pickle.load(open('EAtrained_model.sav', 'rb'))


def EA_Alpha_thal_prediction(input_data):
    # changing the input_data to numpy array
     input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
     input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

     prediction = loaded_model.predict(input_data_reshaped)
     print(prediction)

     if (prediction[0] == 0):
       return 'This person is alpha thalassemia carrier'
     else:
       return 'This person is not alpha thalassemia carrier'
