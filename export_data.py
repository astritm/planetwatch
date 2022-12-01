import streamlit as st
import numpy as np
import pandas as pd
import json
from typing import Counter
import requests
from datetime import datetime, date, timedelta
import time
from operator import add
from collections import defaultdict
import base64
from math import ceil

def write(state): 

 
 st.markdown(
         """
         <h1 style="color: darkblue; text-align:center;">Export Mining Data</h1>
         
         
         """, unsafe_allow_html=True
         
     )
 
 form = st.form(key='submit-form')
 Wallet_address = form.text_input('Please enter your Algorand wallet address without spaces!')
 submit = form.form_submit_button('Submit')

 if submit:
  
  Counter_tx = 0
  dicts={}
  
 
  price_date = {}
    
  if len(Wallet_address) == 58:
    #API request to Algoexplorer.io
    response_algoexplorer = requests.get('https://algoindexer.algoexplorerapi.io/v2/transactions?limit=1000&asset-id=27165954&currency-greater-than=0&address={}'.format(Wallet_address)).text
    response_info_algo = json.loads(response_algoexplorer)

    
    all_transactions = 0
    for transactions in response_info_algo['transactions']:
     all_transactions = all_transactions + 1
    
    with st.spinner(text='In Progress...'):
                    
     response_planets_price_usd = requests.get('https://api.coingecko.com/api/v3/coins/planetwatch/market_chart?vs_currency=usd&days=max', timeout=(2, 5))
     if response_planets_price_usd.status_code != 200:
      st.error("Error getting Planets price from coingeco, try again later...")
      st.stop()
     response_planets_price_usd = response_planets_price_usd.text
     time.sleep(1)
     
     
     response_planets_price_eur = requests.get('https://api.coingecko.com/api/v3/coins/planetwatch/market_chart?vs_currency=eur&days=max', timeout=(2, 5))
     if response_planets_price_eur.status_code != 200:
      st.error("Error getting Planets price from coingeco, try again later...")
      st.stop()
     response_planets_price_eur = response_planets_price_eur.text 
     time.sleep(1)
     
     
     response_planets_price_gbp = requests.get('https://api.coingecko.com/api/v3/coins/planetwatch/market_chart?vs_currency=gbp&days=max', timeout=(2, 5))       
     if response_planets_price_gbp.status_code != 200:
      st.error("Error getting Planets price from coingeco, try again later...")
      st.stop()
     response_planets_price_gbp = response_planets_price_gbp.text
     
     #getting PLANETS:FIAT:DATE from Coingeco
     def planet_price_date(date, currency):
      if currency == 'usd':
       response_info_planets_price = json.loads(response_planets_price_usd)
      elif currency == "eur":
       response_info_planets_price = json.loads(response_planets_price_eur)
      elif currency == 'gbp':
       response_info_planets_price = json.loads(response_planets_price_gbp)
       
      i = len(response_info_planets_price['prices']) - 1
      for price in response_info_planets_price['prices']:
       date_list = datetime.today()
       date_delta = date_list - timedelta(days=i)
       date_delta = date_delta.strftime("%d-%m-%Y")
       price_d = price[1]
       price_d = float(round(price_d, 4))
       price_date[date_delta] = price_d
       i-= 1
      return (price_date[date])
     
     index = 0
                     
     
     for transactions in response_info_algo['transactions']:
      amount = transactions['asset-transfer-transaction']['amount']
      amount = amount / 1000000
      amount = round (amount, 2)

        
      timestamp = transactions['round-time']
      date_txid = datetime.fromtimestamp(timestamp)
      date_txid = date_txid.strftime("%d-%m-%Y")

      Counter_tx = Counter_tx + 1
      
      price_usd = planet_price_date(date_txid, 'usd')
      price_eur = planet_price_date(date_txid, 'eur')
      price_gbp = planet_price_date(date_txid, 'gbp')
     
      
      if transactions['asset-transfer-transaction']['receiver'] == Wallet_address:
         Total_usd = round(price_usd * amount, 3)
         Total_eur = round(price_eur * amount, 3)
         Total_gbp = round(price_gbp * amount, 3)
         amount = str(amount)
         price_usd = str(price_usd)
         Total_usd = str(Total_usd)
         Total_eur = str(Total_eur)
         Total_gbp = str(Total_gbp)
         dicts[index]={"date":date_txid, "price/usd":price_usd, "amount":amount, "usd": Total_usd, "eur": Total_eur, "gbp": Total_gbp, "in/out": "received" }
       
              
      if transactions['asset-transfer-transaction']['receiver'] != Wallet_address:
         Total_usd = round(price_usd * amount, 3)
         Total_eur = round(price_eur * amount, 3)
         Total_gbp = round(price_gbp * amount, 3)
         amount = str(amount)
         price_usd = str(price_usd)
         Total_usd= str(Total_usd)
         Total_eur = str(Total_eur)
         Total_gbp = str(Total_gbp)
         dicts[index]={"date":date_txid, "price/usd":price_usd, "amount":amount, "usd": Total_usd, "eur": Total_eur, "gbp": Total_gbp, "in/out": "sent" }
      
      
      
      index = index + 1
      

    df = pd.DataFrame.from_dict(dicts, orient='index')
    st.dataframe(df)
    today = date.today()
    d = today.strftime("%b-%d-%Y")
   
   
    def get_table_download_link_csv(df):
     csv = df.to_csv().encode()
     b64 = base64.b64encode(csv).decode()
     href = f'<a href="data:file/csv;base64,{b64}" download="wallet_{Wallet_address}_{d}.csv" target="_blank"><p align="right">download...</p></a>'
     return href
     
    st.markdown(get_table_download_link_csv(df), unsafe_allow_html=True)


    
