import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("model.pkl")

st.title("❤️ Heart Disease Predictor")

input_data = st.text_input("Enter Patient's data to prdict:")

if st.button("Predict"):
    try:
        values = np.array([float(i) for i in input_data.split(",")]).reshape(1, -1)
        prediction = model.predict(values)[0]

        if prediction == 1:
            st.error("⚠️ Person has Heart Disease")
        else:
            st.success("✅ Person does NOT have any Heart Disease")

    except Exception as e:
        st.error(f"Invalid input. Please enter 13 comma-separated values.\n\nError: {e}")
