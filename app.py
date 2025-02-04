import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open(r"C:\Users\Ranjan kumar pradhan\.vscode\RFC_Model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Title of the app
st.title("Stroke Risk Prediction API")

# Collect user input
def user_input():
    age = st.slider("Age", 18, 90, 30)
    gender = st.selectbox("Gender", ["Female", "Male", "Other"])
    work_type = st.selectbox("Work Type", ["Private", "Never Worked", "Government", "Children", "Self-employed"])
    avg_glucose = st.number_input("Average Glucose Level", min_value=50.0, max_value=300.0, value=100.0)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
    physical_activity = st.selectbox("Physical Activity", ["Sedentary", "Light", "Active", "Moderate"])
    dietary_habits = st.selectbox("Dietary Habits", ["Non-Vegetarian", "Vegetarian", "Mixed"])
    alcohol_consumption = st.radio("Alcohol Consumption", ["No", "Yes"])
    chronic_stress = st.radio("Chronic Stress", ["No", "Yes"])
    sleep_hours = st.slider("Sleep Hours", 3, 12, 7)
    
    # Encoding categorical variables
    gender_map = {"Female": 0, "Male": 1, "Other": 2}
    work_type_map = {"Private": 0, "Never Worked": 1, "Government": 2, "Children": 3, "Self-employed": 4}
    activity_map = {"Sedentary": 0, "Light": 1, "Active": 2, "Moderate": 3}
    diet_map = {"Non-Vegetarian": 0, "Vegetarian": 1, "Mixed": 2}
    alcohol_map = {"No": 0, "Yes": 1}
    stress_map = {"No": 0, "Yes": 1}
    
    data = np.array([
        age,
        gender_map[gender],
        work_type_map[work_type],
        avg_glucose,
        bmi,
        activity_map[physical_activity],
        diet_map[dietary_habits],
        alcohol_map[alcohol_consumption],
        stress_map[chronic_stress],
        sleep_hours
    ]).reshape(1, -1)
    
    return data

# Predict stroke risk
if st.button("Predict Stroke Risk"):
    input_data = user_input()
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1] * 100  # Get probability of stroke
    
    if prediction[0] == 1:
        st.error(f"⚠️ High Stroke Risk! ({probability:.2f}% chance)")
    else:
        st.success(f"✅ Low Stroke Risk! ({probability:.2f}% chance)")
