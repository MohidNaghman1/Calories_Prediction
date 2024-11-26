import streamlit as st
import pandas as pd
import pickle  # Make sure to import pickle
import os

# Define the base directory and filename
base_dir = '/mount/src/Calories_Prediction'
filename = 'Calories_Prediction.py'

# Construct the full path
model_path = os.path.join(base_dir, filename)

# Function to make predictions
def predict_calories(gender, age, height, weight, duration, heart_rate, body_temp):
    input_data = pd.DataFrame({
        'Gender': [gender],
        'Age': [age],
        'Height': [height],
        'Weight': [weight],
        'Duration': [duration],
        'Heart_Rate': [heart_rate],
        'Body_Temp': [body_temp]
    })
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit app layout
st.set_page_config(page_title="Calories Prediction App", page_icon="🍏")


# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;  /* Light background for the whole app */
        }
        .title {
            font-size: 36px;  /* Slightly smaller font size */
            color: #2E7D32;  /* Darker green for better visibility */
            text-align: center;
            margin: 10px 0;  /* Reduced vertical margin */
            font-family: 'Arial', sans-serif;
        }
  .input-title {
    font-size: 28px;  /* Increase font size */
    font-weight: bold;  /* Make title bold */
    color: #e6ede7 !important;  /* Lighter color for contrast */
    text-align: center;  /* Center align */
    margin: 20px 0;  /* Add margin for spacing */
    padding: 10px;  /* Add padding for better touch */
    background-color: #458a4d;  /* Light green background */
    border-radius: 8px;  /* Rounded corners */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);  /* Subtle shadow for depth */
}
        .description {
            font-size: 22px;
            text-align: center;
            color: #89ad92;  /* Darker color for readability */
            margin-bottom: 40px;
            font-family: 'Arial', sans-serif;
        }
        .input-section {
            padding: 30px;
            border-radius: 15px;
            background-color: #4a8057;  /* White background for contrast */
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);  /* Shadow for depth */
            margin: auto;
            max-width: 600px;  /* Limit width for better layout */
            border: 1px solid #e0e0e0;  /* Light border */
        }
        .input-title {
            font-size: 24px;
            color: #2E7D32;
            text-align: center;
            margin-bottom: 20px;
        }
        .stTextInput, .stNumberInput {
            border: 1px solid #ccc;  /* Light border for inputs */
            border-radius: 5px;  /* Rounded corners for inputs */
            padding: 10px;  /* Padding inside inputs */
            margin-bottom: 15px;  /* Space between inputs */
            width: calc(100% - 22px);  /* Full width, accounting for padding and border */
        }
        .stTextInput:focus, .stNumberInput:focus {
            border-color: #4CAF50;  /* Change border color on focus */
            box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);  /* Subtle shadow on focus */
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="title">🍏 Calories Prediction App</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Enter your details below to predict calories burned during your activities!</div>', unsafe_allow_html=True)

# Input section
with st.container():
    st.markdown('<div class="input-title">User Input</div>', unsafe_allow_html=True)    
    gender = st.selectbox("Gender", options=["Male", "Female"])
    age = st.number_input("Age", min_value=1, max_value=120, placeholder="Enter your age")
    height = st.number_input("Height (cm)", min_value=50, max_value=250, placeholder="Enter your height in cm")
    weight = st.number_input("Weight (kg)", min_value=30, max_value=300, placeholder="Enter your weight in kg")
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=300, placeholder="Enter duration in minutes")
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, placeholder="Enter your heart rate")
    body_temp = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=42.0, placeholder="Enter body temperature in °C")


    st.markdown('</div>', unsafe_allow_html=True)  # Close the input section

# Convert gender to numerical values
gender_numeric = 1 if gender == "Male" else 0

if st.button("Predict"):
    calories = predict_calories(gender_numeric, age, height, weight, duration, heart_rate, body_temp)
    
    # Enhanced output message
    st.markdown(
        f"<h3 style='color: #4CAF50;'>🎉 Predicted Calories Burned: <strong>{calories:.2f}</strong> kcal! 🎉</h3>",
        unsafe_allow_html=True
    )
