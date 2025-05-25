import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("model.pkl")

st.title("Logistic Regression Predictor")

input_data = st.text_input("Enter comma-separated values:")

if st.button("Predict"):
    try:
        x = np.array([float(i) for i in input_data.split(",")]).reshape(1, -1)
        prediction = model.predict(x)
        st.write("Prediction:", prediction[0])
    except:
        st.error("Please enter valid comma-separated numbers.")
