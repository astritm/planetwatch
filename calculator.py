import streamlit as st
import os
import requests
import json
import pandas as pd


def write(state):

 st.markdown(
          """
          <h2 style="color: darkblue; text-align:center;">PLANETS calculator</h2>
         
         
         """, unsafe_allow_html=True
   
      )
 st.write ("--------")
    
#API request to Coingecko PLANETS:USD

 request_vs_currencies = requests.get('https://api.coingecko.com/api/v3/simple/supported_vs_currencies')
 vs_currencies = json.loads(request_vs_currencies.text)
 #st.write(vs_currencies)
 
 currency = st.selectbox('Convert PLANETS to:', options=list(vs_currencies))
 
 def planet_price(vs_currency):
  #vs_currency = 'usd'
  request_price = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=planetwatch&vs_currencies={}'.format(vs_currency))
  if request_price.status_code != 200: 
   st.error("Error getting API data. Try again later...")
   st.stop()
  price = json.loads(request_price.text)
  #st.write(price)
  return price['planetwatch'][vs_currency]

 
 
 form = st.form(key='planets-form')
 planets = form.number_input('Enter the amount of planets:', value=1)
 submit = form.form_submit_button('Submit')

 if submit:
   
   st.write(pd.DataFrame({
   "amount": [planets],    
   "planets:{}".format(currency): [planet_price(currency)],         
   currency: [planet_price(currency) * planets]

  }))

