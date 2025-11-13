import pandas as pd
import numpy as np
import pickle
import streamlit as st

with open('finalized_model_lr.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Shortlisting Universities Based on your profile Score')

st.sidebar.header('USER INPUT')

def user_input():

    gre = st.sidebar.number_input('GRE_SCORE', min_value=0, max_value=1000,value=50)
    toefl = st.sidebar.number_input('TOEFL_SCORE',min_value=0, max_value=1000,value=50)
    u_rating = st.sidebar.number_input('UNIVERSITY_RATING', min_value=0, max_value=1000,value=50)
    sop = st.sidebar.number_input('SOP', min_value=0, max_value=1000,value=50)
    lor = st.sidebar.number_input('LetterOfRecommendation', min_value=0, max_value=1000,value=50)
    cgpa = st.sidebar.number_input('CGPA', min_value=0, max_value=1000,value=50)
    research = st.sidebar.number_input('Research', min_value=0, max_value=1000,value=50)   

    data = {'GRE_SCORE': gre,'TOEFL_SCORE': toefl, 'UNIVERSITY_RATING': u_rating,'SOP': sop,'LetterOfRecommendation': lor,'CGPA': cgpa,'Research': research}

    features = pd.DataFrame(data, index=[0])
    
    return features


input_df = user_input()

st.subheader('USER INPUT PARAMETERS')
st.write(input_df)

predictions = model.predict(input_df)

data = pd.DataFrame()
data['Admit_probability'] = predictions

st.subheader('PREDICTION')
st.write(data)









