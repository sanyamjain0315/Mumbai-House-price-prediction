import streamlit as st
import joblib

model=joblib.load('Mumbai House Prices')

st.title('Mumbai house price predictor')
st.text('This model can predict the price of a house in Mumbai by accepting info such as no. of bedrooms, area, parking space and other details.')
bedrooms=st.slider('Select no. of bedrooms',1,10)
condition=st.radio('Condition:',('New','Resale'))
gym=st.radio('Gym:',('Yes','No'))
lift=st.radio('Lift available:',('Yes','No'))
parking=st.radio('Parking available:',('Yes','No'))
staff=st.radio('Maintenence staff:',('Yes','No'))
security=st.radio('24x7 Security:',('Yes','No'))
play=st.radio('Children play area:',('Yes','No'))
club=st.radio('Clubhouse:',('Yes','No'))
intercom=st.radio('Intercom:',('Yes','No'))
garden=st.radio('Landscaped garden:',('Yes','No'))
indoorgame=st.radio('Indoor games:',('Yes','No'))
gas=st.radio('Gas connection:',('Yes','No'))
track=st.radio('Jogging track:',('Yes','No'))
pool=st.radio('Swimming pool:',('Yes','No'))
area=st.slider('Select the area',200,9000)
x=[bedrooms,condition,gym,lift,parking,staff,security,play,club,intercom,garden,indoorgame,gas,track,pool,area]
y=model.predict([x])
if st.button('Predict'):
  st.success(y[0])
