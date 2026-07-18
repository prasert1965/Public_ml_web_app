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
loaded_model = pickle.load(open('D:/WorkAdaboost/EAtrained_model.sav', 'rb'))

input_data = (30,44.2,14.5,5.41,81.7,26.8,32.8,14)

# changing the input_data to numpy array


input_data_as_numpy_array = np.asarray(input_data)

print(input_data_as_numpy_array)

# reshape the array as we are predicting for one instance

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

print(input_data_reshaped)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('This person is Alpha Thalassemia Triat')
else:
  print('This person is Normal')