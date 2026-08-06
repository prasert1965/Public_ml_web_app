# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:20:43 2024

@author: Administrator
"""

import numpy as np
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import tempfile
from fpdf import FPDF
import streamlit.components.v1 as components
from datetime import datetime
current_time = datetime.now()
loaded_model = pickle.load(open('EAtrained_model.sav', 'rb'))

def EA_Alpha_thal_prediction(input_data):
  

    # changing the input_data to numpy array
     input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
     input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

     prediction = loaded_model.predict(input_data_reshaped)
     print(input_data_as_numpy_array)
     print(prediction)

     if (prediction[0] == 0):
      return 'This person is alpha thalassemia carrier'
     else:
       return 'This person is not alpha thalassemia carrier'
  
   
def main():

    # giving a title  
    st.title('Web for prediction Alpha Thalassemia carrier')   
    
    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    with col1:
         AGE = st.text_input('AGE (years)')
    with col2:
         HCT = st.text_input('Hematocrit (%)')
    with col3:
         HGB = st.text_input('Hemaglobin (g/dl)')
    with col4:
         RBC = st.text_input('RBC count(10^6 cells/cumm')
    with col1:
         MCV = st.text_input('MCV (fl)')
    with col2:
         MCH = st.text_input('MCH (pg)')
    with col3:
         MCHC = st.text_input('MCHC (g/dl)')
    with col4:
         RDW = st.text_input('RDW (fl)')
       
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction 
        
    if st.button('Prediction result Pls. Click'):        
       diagnosis = EA_Alpha_thal_prediction([AGE, HCT, HGB, RBC, MCV, MCH, MCHC, RDW])               
       st.success(diagnosis)
       
    col1, col2, col3, = st.columns(3)
    with col1:
          st.write('Predicted by ..Phrae ADA ML.. ') 
          st.write(f"**Date Prediction:** {current_time}")
    with col2:
          st.write('Reported by ............................ ')   
    with col3:
          st.write('Approved by ............................ ')

if __name__ == '__main__':
    main() 
#st.title("รายงานผลการทำนาย")
# สร้างปุ่มพิมพ์หน้าเว็บ
components.html("""
    <button onclick="window.parent.print()" style="
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;">
        🖨️ พิมพ์รายงาน (Print / Save as PDF)
    </button>
""", height=60)
