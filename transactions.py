import streamlit as st
import numpy as np
import pandas as pd
import json
from typing import Counter
import requests
from datetime import datetime
import time
import html
from operator import add
import os



def write(state):

  #Get PLANET prices from Coingecko
 def planet_price(vs_currency):
   request_price = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=planetwatch&vs_currencies={}'.format(vs_currency))
   if request_price.status_code != 200: 
    st.error("Error getting API data. Try again later...")
    st.stop()
   price = json.loads(request_price.text)
   return price['planetwatch'][vs_currency]
 nrplanets = st.sidebar.number_input("Little PLANETS Calculator", value=1)
 st.sidebar.write(pd.DataFrame({
        'USD': [planet_price('usd') * nrplanets],
        'EUR': [planet_price('eur') * nrplanets],
        'GBP': [planet_price('gbp') * nrplanets]
  
    }))

 st.markdown(
         """
         <h1 style="color: darkblue; text-align:center;">PLANETS Transactions viewer</h1>
         
         
         """, unsafe_allow_html=True
     )

 st.info ("""
         If you want to check the legitimacy of this webapp you can use my own Algorand wallet address below:
         
         **3KBG44MVZSKKOUDW7QJ2QS2FYHFIHNTLT3Q7MTQ2CLG65ZHQ6RL6ENZ7GQ**
         
         And if you want to contribute, that's the address to do it :)
                 
         """
         )
 

 form = st.form(key='my-form')
 count_wallets = form.number_input('How many wallet addresess you want to view:', value=1, max_value=5)
 submit = form.form_submit_button('Submit')
 count = int(count_wallets)
     
 
 Wallet_addresses = []
 for wallets in range(count):
   Wallets = form.text_input('Please enter a your Algorand wallet address {} without spaces!'.format(wallets +1))
   Wallet_addresses.append(Wallets)
 
 run = form.form_submit_button('RUN')
 
 
     
 #Wallet_Address = st.text_input('Please enter a your Algorand wallet address without spaces and hit Enter')
 with st.expander("App Info!"):
  st.info("""
         If you try to get all transactions from Algoexplorer.io for a given wallet address, you will find a lot of transactions with 0 value.
         It's hard to identify the transactions with real amount of PLANETS.
         Therefore I have created this small web app to solve this issue.
         The webapp uses the Algoexplorer API with parameters like PLANETS asset-id: 27165954 and amount greater than 0.
         
         The output will include Date/Time (UTC) of the transaction, the amount of PLANETS received (+) or sent (-) and the transaction-id.
         If you click in the transaction id it will bring you to the Algoexplorer.io to that specific transaction details.
         """     
        )
 
 
 if run:
         
  st.write("---------------------------------------------------")
  col1,col2 = st.columns([8,1])
  
  
  Total_rx = 0
  Total_tx = 0
  Diff = 0
  Counter_tx = 0
  Planets_sensor = 0
  Total_wallets_rx = 0
  Total_wallets_tx = 0
  Total_wallets_Diff = 0
  Total_rewards = 0
  

      
         
  st.write("---------------------------------------------------")
  st.write('***Transactions***')  
  st.write("---------------------------------------------------")
  
  for Wallet_address in Wallet_addresses:
   Total_rx = 0
   Total_tx = 0
   Diff = 0
   Counter_tx = 0
   Planets_sensor = 0
   if len(Wallet_address) == 58:
      if int(count_wallets) > 1:
       st.write('*Address: %s * ' %(Wallet_address))
      #API request to Algoexplorer.io
      response_algoexplorer = requests.get('https://algoexplorerapi.io/idx2/v2/transactions?address={}&asset-id=27165954&currency-greater-than=0&limit=10000'.format(Wallet_address)).text
      response_info_algo = json.loads(response_algoexplorer)
     
      for transactions in response_info_algo['transactions']:
       amount = transactions['asset-transfer-transaction']['amount']
       amount = amount / 1000000
       amount = round (amount, 2)
       timestamp = transactions['round-time']
       your_date = datetime.fromtimestamp(timestamp)
       Counter_tx = Counter_tx + 1
       
       #received from ZW3ISEHZUHPO7OZGMKLKIIMKVICOUDRCERI454I3DB2BH52HGLSO67W754
       if transactions['asset-transfer-transaction']['receiver'] == Wallet_address:
         if transactions['sender'] == 'ZW3ISEHZUHPO7OZGMKLKIIMKVICOUDRCERI454I3DB2BH52HGLSO67W754':
          Planets_sensor = amount + Planets_sensor
         Total_rx = amount + Total_rx
         st.write (your_date, """<font color=green> + </font>""", amount, """<font size="2"><a href="https://algoexplorer.io/tx/%s">%s</a></font>""" %(transactions['id'], transactions['id']), unsafe_allow_html=True)                
       if transactions['asset-transfer-transaction']['receiver'] != Wallet_address:
          Total_tx = amount + Total_tx
          st.write (your_date, """<font color=red> - </font>""", amount, """<font size="2"><a href="https://algoexplorer.io/tx/%s">%s</a></font>""" %(transactions['id'], transactions['id']), unsafe_allow_html=True)
          
  
      Total_rx = round(Total_rx, 2)
      Total_tx = round(Total_tx, 2)
      Diff = Total_rx - Total_tx
      Diff = round(Diff, 2)
      Total_USD_wallet = planet_price('usd') * Diff
      Total_EUR_wallet = planet_price('eur') * Diff
      
      #Total wallets counters
      Total_wallets_rx = Total_rx + Total_wallets_rx
      Total_wallets_tx = Total_tx + Total_wallets_tx
      Total_wallets_Diff = Diff + Total_wallets_Diff
      Total_rewards = Planets_sensor + Total_rewards
      
      
      st.write("---------------------------------------------------")
      with col1:
       if int(count_wallets) > 1:
        st.write('**%s**' %(Wallet_address))
       st.write(pd.DataFrame({
        'Rewarded' : [Planets_sensor],
        'USD' : [Planets_sensor * planet_price('usd')],
        'EUR' : [(Planets_sensor * planet_price('eur'))]
           
       }))
      
      with col1:
       st.write(pd.DataFrame({
       'Received': [Total_rx],
       'Sent': [Total_tx],
       'Wallet' : [Diff]
       
      })) 
      with col1:
       st.write(pd.DataFrame({
       'PLANETS:USD': [planet_price('usd')],
       'Total USD' : [Total_USD_wallet],
       'Total EUR' : [Total_EUR_wallet]
      
       }))
  
  #Total Wallets:
  
  if int(count_wallets) > 1:
   st.write("---------------------------------------------------")
       
   with col1:
       st.write("---------------------------------------------------")
       st.write('**Totals from all Wallets**')
       st.write("---------------------------------------------------")
       st.write(pd.DataFrame({
         'Rewarded' : [Total_rewards],
         'USD' : [Total_rewards * planet_price('usd')],
         'EUR' : [(Total_rewards * planet_price('eur'))]
            
        }))
       
   with col1:
        st.write(pd.DataFrame({
        'Received': [Total_wallets_rx],
        'Sent': [Total_wallets_tx],
        'Wallet' : [Total_wallets_Diff]
        
       })) 
   with col1:
        st.write(pd.DataFrame({
        'PLANETS:USD': [planet_price('usd')],
        'Total USD' : [Total_wallets_Diff * planet_price('usd')],
        'Total EUR' : [(Total_wallets_Diff * planet_price('eur'))]
       
        }))
 
 
