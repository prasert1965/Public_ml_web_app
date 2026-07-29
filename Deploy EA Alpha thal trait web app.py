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
# 1. Define your PDF Generator
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Prediction Analysis Report', border=False, ln=True, align='C')
        self.ln(5)

def generate_pdf(prediction_label, confidence, fig):
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    
    # Add text summary
    pdf.cell(0, 10, f"Model Prediction: {prediction_label}", ln=True)
    pdf.cell(0, 10, f"Confidence Score: {confidence}%", ln=True)
    pdf.ln(5)
    
    # Save Matplotlib figure to a temporary file and add to PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        fig.savefig(tmpfile.name, format="png", bbox_inches='tight')
        # pdf.image(path, x, y, width)
        pdf.image(tmpfile.name, x=15, y=50, w=180) 
    
    # Output PDF as byte string
    return pdf.output(dest='S').dencode('latin-1')

# --- Streamlit UI ---
st.title("Prediction Dashboard")

# Mock Prediction Data
prediction = "High Risk"
score = 88.5

st.subheader("Results")
st.write(f"**Prediction:** {prediction}")
st.write(f"**Confidence:** {score}%")

# Generate a Matplotlib Plot
fig, ax = plt.subplots(figsize=(6, 3.5))
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y, color='crimson', linewidth=2, label="Prediction Curve")
ax.set_title("Forecast Probability Density")
ax.set_xlabel("Time Step")
ax.set_ylabel("Probability")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.6)

# Display Plot in Streamlit App
st.pyplot(fig)

# Generate PDF with Graph included
pdf_data = generate_pdf(prediction, score, fig)

# Download Button
st.download_button(
    label="📄 Download PDF Report (with Graph)",
    data=pdf_data,
    file_name="prediction_report.pdf",
    mime="application/pdf"
)


