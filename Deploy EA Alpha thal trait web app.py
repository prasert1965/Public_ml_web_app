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
       
if __name__ == '__main__':
    main() 
st.title("Prediction Dashboard")

# Your Streamlit UI
st.metric(label="Model Accuracy", value="94.2%", delta="1.2%")
st.line_chart([10, 20, 15, 30, 50, 40])

# Add CSS to customize what gets printed (e.g., hide sidebars & buttons)
st.markdown("""
    <style>
    @media print {
        /* Hide sidebar, navigation bar, and action buttons during print */
        section[data-testid="stSidebar"],
        header,
        footer,
        .stButton,
        [data-testid="stHeader"] {
            display: none !important;
        }
        /* Force full screen layout */
        .main .block-container {
            max-width: 100% !important;
            padding: 0 !important;
        }
    }
    </style>
""", unsafe_unsafe_html=True)

# Print Screen Button via HTML/JS
st.components.v1.html("""
    <button onclick="window.parent.print()" style="
        background-color: #ff4b4b;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: bold;
        cursor: pointer;">
        ๐–จ๏ธ Print Screen to PDF
    </button>
""", height=60)
