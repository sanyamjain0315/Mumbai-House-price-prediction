import streamlit as st
import joblib

model=joblib.load('Mumbai House Prices')

st.title('Mumbai house price predictor')
st.text('This model can predict the price of a house in Mumbai by accepting info such as no. of bedrooms, area, parking space and other details.')
bedrooms=st.slider('Select no. of bedrooms',1,10)
if(st.radio('Condition:',('New','Resale'))=='New'):
  condition=1
else:
  condition=0
if(st.radio('Gym:',('Yes','No'))=='Yes'):
  gym=1
else:
  gym=0
if(st.radio('Lift available:',('Yes','No'))=='Yes'):
   lift=1
else:
   lift=0
if(st.radio('Parking available:',('Yes','No'))=='Yes'):
   parking=1
else:
   parking=0
if(st.radio('Maintenence staff:',('Yes','No'))=='Yes'):
   staff=1
else:
   staff=0
if(st.radio('24x7Security:',('Yes','No'))=='Yes'):
   security=1
else:
   security=0
if(st.radio('Play area:',('Yes','No'))=='Yes'):
   play=1
else:
   play=0
if(st.radio('Clubhouse:',('Yes','No'))=='Yes'):
  club=1
else:
  club=0
if(st.radio('Intercom:',('Yes','No'))=='Yes'):
  intercom=1
else:
  intercom=0
if(st.radio('Landscaped garden:',('Yes','No'))=='Yes'):
  garden=1
else:
  garden=0
if(st.radio('Indoor games:',('Yes','No'))=='Yes'):
  indoorgame=1
else:
  indoorgame=0
if(st.radio('Gas connection:',('Yes','No'))=='Yes'):
  gas=1
else:
  gas=0
if(st.radio('Jogging track:',('Yes','No'))=='Yes'):
  track=1
else:
  track=0
if(st.radio('Swimming pool:',('Yes','No'))=='Yes'):
  pool=1
else:
  pool=0
area=st.slider('Select the area',200,9000)
x=[bedrooms,condition,gym,lift,parking,staff,security,play,club,intercom,garden,indoorgame,gas,track,pool,area]
y=model.predict([x])
if st.button('Predict'):
  st.text('Price of the home in rupees is:')
  st.success(y[0])

  
  
