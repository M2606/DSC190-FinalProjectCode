import pickle
import streamlit as st
import pandas as pd


def main():
    st.title("NYPD Case Outcome Prediction")
    st.subheader("Enter features")
    mos_ethnicity = st.selectbox('Officer Ethnicity', ('Black', 'Hispanic', 'White', 'Other Race', 'Asian', 'American Indian', 'Unknown'))
    mod_gender= st.selectbox('Officer Gender', ('F', 'M', 'Other'))
    complainant_ethnicity = st.selectbox('Complainant Ethnicity', ('Black', 'Hispanic', 'White', 'Other Race', 'Asian', 'American Indian', 'Unknown'))
    complainant_gender = st.selectbox('Complainant Gender', ('Female', 'Male', 'Transman (FTM)', 'Transwoman (MTF)', 'Not described'))
    fado_type = st.selectbox('Offence Type', ('Abuse of Authority', 'Discourtesy', 'Offensive Language', 'Force'))
    mos_age_incident= st.text_input('Officer Age', 50)
    complainant_age_incident=st.text_input('Complainant Age', 50)
    year_received = st.text_input('Year complaint was filed', 2018)
    year_closed = st.text_input('Year complaint was closed', 2018)
    model = pickle.load(open('model.pkl', 'rb'))
    wait_time = int(year_closed) - int(year_received)
    if st.button('Predict Outcome'):

        prediction = model.predict(pd.DataFrame({'mos_ethnicity':mos_ethnicity, 'mos_gender': mod_gender, 'complainant_ethnicity':complainant_ethnicity, 'complainant_gender':complainant_gender,'fado_type':fado_type, 'mos_age_incident':int(mos_age_incident), 'complainant_age_incident':int(complainant_age_incident), 'wait_time':int(wait_time)}, index = [0]))[0]
        if prediction == 0:
            st.success('Complaint is valid')
        if prediction == 1:
            st.success('Complaint is dismissed')
    return "Click predict to make predictions!"

if __name__ == "__main__":
    main()