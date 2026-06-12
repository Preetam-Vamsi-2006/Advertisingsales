import streamlit as st
import joblib
import numpy as np

st.title("Sales Prediction")

# Load model
model = joblib.load('multiple.joblib')

# Input fields
tv = st.number_input("TV Advertising", min_value=0.0, value=100.0)
radio = st.number_input("Radio Advertising", min_value=0.0, value=25.0)

# Predict button
if st.button("Predict"):
    prediction = model.predict([[tv, radio]])[0]
    st.success(f"Predicted Sales: ${prediction:,.2f}")