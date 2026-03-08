import streamlit as st
import joblib
import numpy as np
# load model
model = joblib.load("DecisionTreeClassifier_model.pkl")
st.title("Gaming Addiction Risk Predictor")
st.write("Enter gamer details")

age = st.number_input("Age",min_value=0,max_value=100,value=None,placeholder="Enter age")
gender = st.selectbox("Gender", ["select","Female", "Male"])
weight_change_kg = st.number_input("Weight Change (kg)",min_value=0,value=None,placeholder="Enter weight change")
social_isolation_score = st.number_input("Social Isolation Score",min_value=0,value=None,placeholder="Enter social isolation score")
face_to_face_social_hours_weekly = st.number_input("Face-to-Face Social Hours Weekly",min_value=0,value=None,placeholder="Enter face-to-face social hours")
years_gaming = st.number_input("Years of Gaming",min_value=0,value=None,placeholder="Enter years of gaming")
daily_gaming_hours = st.number_input("Daily Gaming Hours",min_value=0,value=None,placeholder="Enter daily gaming hours")
sleep_hours = st.number_input("Sleep Hours",min_value=0,value=None,placeholder="Enter sleep hours")
eye_strain = st.selectbox("Eye Strain", ["Select", "No", "Yes"])
back_neck_pain = st.selectbox("Back/Neck Pain", ["select", "No", "Yes"])

    

# prediction button
if st.button("Predict Risk Level"):
    
    if gender == "select":
        st.warning("Please select a valid gender.")

    elif eye_strain == "Select":
        st.warning("Please select a valid eye strain option.")

    elif back_neck_pain == "select":
        st.warning("Please select a valid back/neck pain option.")

    elif age == 0 or age is None:
        st.warning("Please enter a valid age.")

    elif weight_change_kg == 0 or weight_change_kg is None:
        st.warning("Please enter a valid weight change.")

    elif social_isolation_score == 0 or social_isolation_score is None:
        st.warning("Please enter a valid social isolation score.")

    elif face_to_face_social_hours_weekly == 0 or face_to_face_social_hours_weekly is None:
        st.warning("Please enter valid face-to-face social hours.")

    elif years_gaming == 0 or years_gaming is None:
        st.warning("Please enter valid years of gaming.")

    elif daily_gaming_hours == 0 or daily_gaming_hours is None:
        st.warning("Please enter valid daily gaming hours.")

    elif sleep_hours == 0 or sleep_hours is None:
        st.warning("Please enter valid sleep hours.")

    else:

        if gender == "Female":
            gender = 0
        else:
            gender = 1

        if eye_strain == "No":
            eye_strain = 0
        else:
            eye_strain = 1

        if back_neck_pain == "No":
            back_neck_pain = 0
        else:
            back_neck_pain = 1

        input_data = np.array([[age,
                                gender,
                                int(weight_change_kg),
                                social_isolation_score,
                                face_to_face_social_hours_weekly,
                                years_gaming,
                                daily_gaming_hours,
                                sleep_hours,
                                eye_strain,
                                back_neck_pain]])

        prediction = model.predict(input_data)

        addiction_level = {
            0: "Low Risk",
            1: "Normal",
            2: "Moderate Addiction",
            3: "Severe Addiction"
        }

        result = int(prediction[0])

        st.success(f"Predicted Addiction Risk Level : {addiction_level[result]}")