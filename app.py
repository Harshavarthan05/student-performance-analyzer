import streamlit as st
import joblib
import pandas as pd

model = joblib.load('model/model.pkl')
num_cols = joblib.load("model/num_cols.pkl")
cat_cols = joblib.load("model/cat_cols.pkl")

st.set_page_config(page_title = 'Student Failure predictor', layout = 'centered')

st.title("Student Failure prediction app")
st.write("Enter student details to predict failure risk")

school = st.selectbox("School", ["GP", "MS"])
sex = st.selectbox("Sex", ['M', 'F'])
age = st.slider("Age", 15,22,18)
address = st.selectbox("Address", ["U", "R"])
famsize = st.selectbox("Family Size", ["LE3", "GT3"])
Pstatus = st.selectbox("Parent Status", ["T", "A"])

Medu = st.slider("Mother Eduction (0-4)", 0,4,2)
Fedu = st.slider("Father Education (0-4)", 0,4,2)
Mjob = st.selectbox("Mother Job", ["teacher", "health", "services", "at_home", "ohter"])
Fjob = st.selectbox("Father Job", ["teacher", "health", "services", "at_home", "others"])
reason = st.selectbox("Reason for School", ["home", "reputation", "course", "other"])
guardian = st.selectbox("Guardian", ["mother", "father", "ohter"])
studytime = st.slider("Study Time (1-4)", 1,4,2)
failures = st.slider("Past Failures", 0,3,0)

schoolsup = st.selectbox("School Support", ["yes", "no"])
famsup = st.selectbox("Family Support", ["yes", "no"])
paid = st.selectbox("Paid Classes", ["yes", "no"])
activities = st.selectbox("Extra Activities", ["yes", "no"])
nursery = st.selectbox("Nursery School", ["yes", "no"])
higher = st.selectbox("Higher Education", ["yes", "no"])
internet = st.selectbox("Internet Access", ["yes", "no"])
romantic = st.selectbox("Romantic Relationship", ["yes", "no"])

traveltime = st.slider("Travel Time (1–4)", 1, 4, 1)
famrel = st.slider("Family Relationship (1–5)", 1, 5, 3)
freetime = st.slider("Free Time (1–5)", 1, 5, 3)
goout = st.slider("Going Out (1–5)", 1, 5, 3)
Dalc = st.slider("Workday Alcohol (1–5)", 1, 5, 1)
Walc = st.slider("Weekend Alcohol (1–5)", 1, 5, 1)
health = st.slider("Health (1–5)", 1, 5, 3)

absences = st.slider("Absences", 0,100,5)
G1 = st.slider("G1 Grade", 0,20,10)
G2 = st.slider("G2 Grade", 0,20,10)
G3 = st.slider("G3 Grade", 0,20,10)

input_data = pd.DataFrame([{
    "School" : school,
    "sex": sex,
    "age" : age,
    "address": address,
    "famsize":famsize,
    "Pstatus":Pstatus,
    "Medu":Medu,
    "Fedu":Fedu,
    "Mjob": Mjob,
    "Fjob": Fjob,
    "reason":reason,
    "guardian": guardian,
    "traveltime":traveltime,
    "StudyTime":studytime,
    "Failures": failures,
    "schoolsup":schoolsup,
    "famsup":famsup,
    "paid": paid,
    "activities": activities,
    "nursery": nursery,
    "higher": higher,
    "internet": internet,
    "romantic": romantic,
    "famrel": famrel,
    "freetime": freetime,
    "goout": goout,
    "Dalc": Dalc,
    "Walc": Walc,
    "health": health,
    "absences": absences,
    "G1":G1,
    "G2":G2,
    "G3":G3
}])

for col in num_cols:
    if col not in input_data.columns:
        input_data[col] = 0

for col in cat_cols:
    if col not in input_data.columns:
        input_data[col] = "no"


if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"Likely to fail (risk: {prob:.2%})")
    else:
        st.success(f"Likely to pass (risk: {prob:.2%})")