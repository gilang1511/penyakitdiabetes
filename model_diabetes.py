import streamlit as st #Untuk pembuatan web
import pandas as pd #Pembacaan data
import pickle #Pembacaan Model
from sklearn.preprocessing import LabelEncoder

model_diabetes = pickle.load(open('diabetes_model.sav', 'rb'))

st.title('Data Prediksi Diabetes')

#Membagi kolom 
col1, col2 = st.columns (2)

with col1 :
    Pregnancies = st.text_input('input nilai Pregnancies/kehamilan')

with col2 :
    Glucose = st.text_input('input nilai Glucose/gula darah')

with col1 :
    BloodPressure = st.text_input('input nilai BloodPressure/tekanan darah')
with col2 :
    SkinThickness = st.text_input('input nilai SkinThickness/ketebalan kulit')

with col1 :
    Insulin = st.text_input('input nilai Insulin/kadar insulin dalam darah')

with col2 :
    BMI = st.text_input('input nilai BMI/Body max Indexs')

with col1 :
    DiabetesPedigreeFunction = st.text_input('input nilai Diabetes Pedigree Function')
with col2 :
    Age = st.text_input('input nilai Age/Usia')

#Code untuk prediksi

diab_diagnosis = ''

#membuat tombol untuk predikisi diabetes
if st.button("Prediksi Diabetes"):
    diab_prediction = model_diabetes.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction,Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Terkena diabetes'
    else :
        diab_diagnosis = 'Tidak terkena diabetes'
    st.success(diab_diagnosis)

