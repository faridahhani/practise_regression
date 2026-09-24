import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Student CGPA Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student CGPA Prediction")
st.write(
    "Enter a student's study hours and attendance to predict CGPA "
    "using the trained Multiple Linear Regression model."
)

@st.cache_resource
def load_model():
    return joblib.load("cgpa_linear_regression_model.pkl")

model = load_model()

study_hours = st.number_input(
    "Study Hours per Week",
    min_value=2.0,
    max_value=24.0,
    value=11.0,
    step=0.5
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=50.0,
    max_value=100.0,
    value=82.0,
    step=1.0
)

if st.button("Predict CGPA"):
    input_data = pd.DataFrame({
        "study_hours": [study_hours],
        "attendance": [attendance]
    })

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")
    st.metric("Predicted CGPA", f"{prediction:.2f}")

    if prediction >= 3.50:
        st.success("Predicted performance: Excellent")
    elif prediction >= 3.00:
        st.info("Predicted performance: Good")
    elif prediction >= 2.00:
        st.warning("Predicted performance: Satisfactory")
    else:
        st.error("Predicted performance: Needs attention")

st.caption(
    "Practice model using a synthetic dataset. "
    "The model uses study_hours and attendance after feature selection."
)
