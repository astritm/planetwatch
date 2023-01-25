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
import asyncio
import aiohttp

# 3KBG44MVZSKKOUDW7QJ2QS2FYHFIHNTLT3Q7MTQ2CLG65ZHQ6RL6ENZ7GQ
  
def write(state): 
 st.markdown(
         """
         <h2 style="color: darkblue; text-align:center;">Export Transaction Data</h2>
         
         
         """, unsafe_allow_html=True
         
     )

 
 form = st.form(key='submit-form', clear_on_submit=False)
 wallet_address = form.text_input('Please enter your Algorand wallet address without spaces!')
 submit = form.form_submit_button('Submit')

 if submit:
    
  if len(wallet_address) == 58:
       
    with st.spinner(text='Getting data from the Algorand Blockchain...'):
     
      def get_date_from_number(number):
         today = datetime.today()
         date_delta = today - timedelta(days=number)
         return date_delta.strftime("%d-%m-%Y")
    
      
      
      #getting PLANETS:FIAT:DATE from Coingeco and cashing for 6h
      @st.cache(suppress_st_warning=True, allow_output_mutation=True, ttl=20000)
      def planet_price_date(vs_currency):
         prices_dates={}
         request = requests.get(f'https://api.coingecko.com/api/v3/coins/planetwatch/market_chart?vs_currency={vs_currency}&days=max')
         response = request.text
         prices = json.loads(response)
         prices = prices['prices']
         counter = 0
         for i in prices:
            date = str(get_date_from_number(len(prices) - counter -1))
            price = i[1]
            price = float(round(price, 3))
            prices_dates[date] = price
            counter += 1
         return prices_dates
         
      time.sleep(2)
      prices_usd = planet_price_date("usd")
      time.sleep(2)
      prices_eur = planet_price_date("eur")
      time.sleep(2)
      prices_gbp = planet_price_date("gbp")
      time.sleep(2)

      dicts={}
      # @st.cache(suppress_st_warning=True, allow_output_mutation=True, ttl=20000)
      async def transactions(wallet_address):
         async with aiohttp.ClientSession() as session:
            async with session.get(f'https://algoindexer.algoexplorerapi.io/v2/transactions?limit=2000&asset-id=27165954&currency-greater-than=0&address={wallet_address}') as request:
                  response_info = await request.json()
                  index = 0
                  counter_tx = 0
                  for transactions in response_info['transactions']:
                     amount = transactions['asset-transfer-transaction']['amount']
                     amount = amount / 1000000
                     amount = round (amount, 2)
                     timestamp = transactions['round-time']
                     date_txid = datetime.fromtimestamp(timestamp)
                     date_txid = date_txid.strftime("%d-%m-%Y")

                     counter_tx += 1
                     price_usd = prices_usd[str(date_txid)]
                     price_eur = prices_eur[str(date_txid)]
                     price_gbp = prices_gbp[str(date_txid)]

                     if transactions['asset-transfer-transaction']['receiver'] == wallet_address:
                        Total_usd = round(price_usd * amount, 3)
                        Total_eur = round(price_eur * amount, 3)
                        Total_gbp = round(price_gbp * amount, 3)
                        amount = str(amount)
                        price_usd = str(price_usd)
                        price_eur = str(price_eur)
                        price_gbp = str(price_gbp)
                        Total_usd = str(Total_usd)
                        Total_eur = str(Total_eur)
                        Total_gbp = str(Total_gbp)
                        dicts[index]={"date":date_txid, "price/usd":price_usd, "price/eur":price_eur, "price/gbp":price_gbp, "amount":amount, "usd": Total_usd, "eur": Total_eur, "gbp": Total_gbp, "in/out": "received" }
                        
                     if transactions['asset-transfer-transaction']['receiver'] != wallet_address:
                        Total_usd = round(price_usd * amount, 3)
                        Total_eur = round(price_eur * amount, 3)
                        Total_gbp = round(price_gbp * amount, 3)
                        amount = str(amount)
                        price_usd = str(price_usd)
                        price_eur = str(price_eur)
                        price_gbp = str(price_gbp)
                        Total_usd= str(Total_usd)
                        Total_eur = str(Total_eur)
                        Total_gbp = str(Total_gbp)
                        dicts[index]={"date":date_txid, "price/usd":price_usd, "price/eur":price_eur, "price/gbp":price_gbp, "amount":amount, "usd": Total_usd, "eur": Total_eur, "gbp": Total_gbp, "in/out": "sent" }   
                     index += 1
         return dicts
               
      df = pd.DataFrame.from_dict(asyncio.run(transactions(wallet_address)), orient='index')
      st.dataframe(df, height = 500)
      today = date.today()
      d = today.strftime("%b-%d-%Y")
      
      
      def get_table_download_link_csv(df):
         csv = df.to_csv().encode()
         b64 = base64.b64encode(csv).decode()
         href = f'<a href="data:file/csv;base64,{b64}" download="wallet_{wallet_address}_{d}.csv" target="_blank"><p align="right">CSV Download</p></a>'
         return href
      
      st.markdown(get_table_download_link_csv(df), unsafe_allow_html=True)
      


    
