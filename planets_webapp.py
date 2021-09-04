import streamlit as st
import numpy as np
import pandas as pd
import json
from typing import Counter
import requests
from datetime import datetime
import time


st.set_page_config(page_title="Planets",layout='centered')


   

st.markdown(
        """
        # $PLANETS Transactions Viewer!
        
        """
    )

Wallet_Address = st.text_input('Please enter a your Algorand wallet address without spaces and hit Enter')

st.info("""
        If you try to get all transactions from Algoexplorer.io for a given wallet address, you will find a lot of transactions with 0 value.
        It's hard to identify the transactions with real amount of PLANETS.
        Therefore I have created this small web app to solve this issue.
        The webapp uses the Algoexplorer API with parameters like PLANETS asset-id: 27165954 and amount greater than 0.
        
        The output will include Date/Time (UTC) of the transaction, the amount of PLANETS received (+) or sent (-) and the transaction-id.
        If you click in the transaction id it will bring you to the Algoexplorer.io to that specific transaction details.
        """     
       )

st.info ("""
        If you want to check the legitimacy of this webapp you can use my own Algorand wallet address below:
        
        **3KBG44MVZSKKOUDW7QJ2QS2FYHFIHNTLT3Q7MTQ2CLG65ZHQ6RL6ENZ7GQ**
        
        And if you want to contribute, that's the address to do it :)
                
        """
        )

#st.sidebar.title("PLANETS Transaction Formater")
st.sidebar.write("")
st.sidebar.title("About")

st.sidebar.info(
            """
            The webapp is created by Astr0 to help the PW community and it is ad-free
            and open-source. 
            
            If you find the app useful you can support me in the 
            Algorand wallet address in the description.
                     
            You can find the source code and contribute [here](https://github.com/astritm/planetwatch).  
            
            Special thanks to the PW discord mods @feralfether, @inforkill, @Wagner, @Annie^^ and many more who have actively or passively
            contributed to the PlanetWatch project.
            
            Thanks to **Chris Crypto Coffee** for making such a lovely instructional and informative videos about PlanetWatch in general.
            Please check his channel in the following link:
            https://bit.ly/2WNAwxk
            
            If you are not yet aware about PlanetWatch project, please check it here https://planetwatch.io/ 
            Where you can buy different types of Airquality sensor and correspoding licenses.
            Running a sensor and actively sending data streams to planetwatch you will be rewarded with PLANETS tokens.
            """
            )


Total_rx = 0
Total_tx = 0
Diff = 0
Counter_tx=0

if len(Wallet_Address) == 58:

    #API request to Algoexplorer.io
    response_algoexplorer = requests.get('https://algoexplorerapi.io/idx2/v2/transactions?address={}&asset-id=27165954&currency-greater-than=0&limit=10000'.format(Wallet_Address)).text
    response_info_algo = json.loads(response_algoexplorer)
    
    #API request to BitFinex PLANETS:USD
    response_bitfinex = requests.get('https://api-pub.bitfinex.com/v2/ticker/tPLANETS:USD').text
    response_info_bitfinex = json.loads(response_bitfinex)
    last_price=response_info_bitfinex[6]
    
    st.write("---------------------------------------------------")

    for transactions in response_info_algo['transactions']:
     amount = transactions['asset-transfer-transaction']['amount']
     amount = amount / 1000000
     amount = round (amount, 2)
     timestamp = transactions['round-time']
     your_date = datetime.fromtimestamp(timestamp)
     Counter_tx = Counter_tx + 1
     if transactions['asset-transfer-transaction']['receiver'] == Wallet_Address:
        Total_rx = amount + Total_rx
        st.write (your_date, """<font color=green> + </font>""", amount, """<font size="2"><a href="https://algoexplorer.io/tx/%s">%s</a></font>""" %(transactions['id'], transactions['id']), unsafe_allow_html=True)
                            
     if transactions['asset-transfer-transaction']['receiver'] != Wallet_Address:
        Total_tx = amount + Total_tx
        st.write (your_date, """<font color=red> - </font>""", amount, """<font size="2"><a href="https://algoexplorer.io/tx/%s">%s</a></font>""" %(transactions['id'], transactions['id']), unsafe_allow_html=True)
        

    Total_rx = round(Total_rx, 2)
    Total_tx = round(Total_tx, 2)
    Diff = Total_rx - Total_tx
    Diff = round(Diff, 2)
    Total_USD_wallet=last_price * Diff
    st.write("---------------------------------------------------")
    st.write('Summary')
    st.write(pd.DataFrame({
    'Received': [Total_rx],
    'Sent': [Total_tx],
    'In wallet:': [Diff],
    'PLANETS:USD': [last_price],
    'Total USD:' : [Total_USD_wallet]
    
   
    }))
    
   
@st.cache(allow_output_mutation=True)
def Pageviews():
    return []

pageviews=Pageviews()
pageviews.append('dummy')

try:
    st.sidebar.markdown('Page viewed = {} times.'.format(len(pageviews)))
except ValueError:
    st.sidebar.markdown('Page viewed = {} times.'.format(1))
