import streamlit as st
import pickle

st.title ("Gender prediction using Decision tree classifier")

weight=st.number_input('Enter Weight (in kg)',0,150,10,10)
height=st.number_input('Enter Height (in cm)',0,250,10,10)

#weight=st.slider('Enter Weight',0,150)
#height=st.slider('Enter Height',0,250)

loadedmodel=pickle.load(open('finalmodel.pkl','rb'))
pred=loadedmodel.predict([[weight,height]])

st.write('The gender of the person is ',pred[0])