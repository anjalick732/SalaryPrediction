import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model.pkl")

st.title("💼 Employee Salary Prediction")
st.markdown("Enter the employee's details to predict the estimated salary.")

experience = st.slider("Years of Experience", 0, 20, 1)

if st.button("Predict Salary"):
    prediction = model.predict(np.array([[experience]]))
    st.success(f"Estimated Salary: ₹{int(prediction[0])}")