import streamlit as st
import os
import requests
import json
import pandas as pd


def write(state):
 st.markdown(
          """
          <h1 style="color: darkblue; text-align:center;">PLANETS to FIAT calculator</h1>
         
         
         """, unsafe_allow_html=True
          
          
      )
 st.write ("--------")
    
#API request to BitFinex PLANETS:USD
 response_bitfinex = requests.get('https://api-pub.bitfinex.com/v2/ticker/tPLANETS:USD').text
 response_info_bitfinex = json.loads(response_bitfinex)
 last_price=response_info_bitfinex[6]
  
 #API to get EUR-USD rate
 response_eurusd = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/usd.json').text
 response_info_eurusd = json.loads(response_eurusd)
 eur_usd = response_info_eurusd['usd']
 
 #API to get USD-CAD
 response_usdcad = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/cad.json').text
 response_info_usdcad = json.loads(response_usdcad)
 usd_cad = response_info_usdcad['cad']
 
  #API to get USD-GBP
 response_usdgbp = requests.get(' https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/gbp.json').text
 response_info_usdgbp = json.loads(response_usdgbp)
 usd_gbp = response_info_usdgbp['gbp']
 
 #API to get USD-CHF
 response_usdchf = requests.get(' https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/chf.json').text
 response_info_usdchf = json.loads(response_usdchf)
 usd_chf = response_info_usdchf['chf']
 

 
 
 form = st.form(key='planets-form')
 planets = form.number_input('Enter the amount of planets:', value=0)
 submit = form.form_submit_button('Submit')

 if submit:
  planets_usd = last_price * planets
  planets_eur = planets_usd / eur_usd
  planets_cad = planets_usd * usd_cad
  planets_gbp = planets_usd * usd_gbp
  planets_chf = planets_usd * usd_chf
 
  st.write(pd.DataFrame({
   'EUR': [planets_eur],
   'USD': [planets_usd],
   'CAD': [planets_cad],
   'GBP': [planets_gbp],
   'CHF': [planets_chf]
  }).round(decimals=2))

