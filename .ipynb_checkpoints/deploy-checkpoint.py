import streamlit as st
import requests
from streamlit_lottie import st_lottie
import joblib
import numpy as np
from PIL import Image

image = Image.open('./img/funding.png')
st.set_page_config(page_title='Loan Prediction', page_icon=image)


def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def prepare_input_data_for_model(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area):
    if Gender == 'Male':
        Gender = 1
    else:
        Gender = 0

    if Married == 'Yes':
        Married = 1
    else:
        Married = 0


    if Dependents == '0':
        Dependents = 0
    elif Dependents == '1':
        Dependents = 1
    elif Dependents == '2':
        Dependents = 2
    else:
        Dependents = 3


    if Education == 'Graduate':
        Education = 0
    else:
        Education = 1


    if Self_Employed == 'Yes':
        Self_Employed = 1
    else:
        Self_Employed = 0


    if Property_Area == 'Urban':
        Property_Area = 2
    elif Property_Area == 'Rural':
        Property_Area = 0
    else:
        Property_Area = 1



    Features = [Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome,
         CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]
    sample = np.array(Features).reshape(-1, len(Features))
    return sample


loaded_model = joblib.load(open("loan_predition_model", 'rb'))
st.title('Loan Prediction System')
animation_header = load_lottie("https://assets6.lottiefiles.com/packages/lf20_azmc2roh.json")
st_lottie(animation_header, speed=1, height=200, key="initial")
lottie_link = "https://assets8.lottiefiles.com/packages/lf20_4wDd2K.json"
animation = load_lottie(lottie_link)
st.write('---')
st.subheader('Enter Your Information to predict your loan statues :')
with st.container():
    right_column, left_column = st.columns(2)
    with right_column:

        Gender = st.radio('Gender :', ['Female', 'Male'])
        Married = st.radio('Married :', ['Yes', 'No'])
        Dependents = st.selectbox('Dependents : ', ['0', '1', '2', '3+'])
        Education = st.radio('Education :', ['Graduate', 'not Graduate'])
        Self_Employed = st.radio('Self_Employed:', ['Yes', 'No'])
        ApplicantIncome = st.number_input('ApplicantIncome : ', value=0)
        CoapplicantIncome = st.number_input('CoapplicantIncome : ', value=0)
        LoanAmount = st.number_input('LoanAmount : ', value=0)
        Loan_Amount_Term = st.number_input('Loan_Amount_Term : ', value=0)
        Credit_History = st.radio('Credit_History :', [0, 1])
        Property_Area = st.selectbox('Property_Area : ', ['Urban', 'Rural', 'Semiurban'])

        sample = prepare_input_data_for_model(Gender, Married, Dependents, Education, Self_Employed,
                                              ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area)

    with left_column:
        st_lottie(animation, speed=1, height=400, key="secoend")

    if st.button('predict'):
        pp = loaded_model.predict(sample)
        if pp == 1:
            st.write("congratulation, Your Loan has been acceptd")
            st.balloons()
            st.snow()
        else:
            st.write("sorry..!! Your Loan has been refused")
