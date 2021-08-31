import streamlit as st
import numpy as np
import pandas as pd
import json
from typing import Counter
import requests
from datetime import datetime
import time

#st.set_page_config(layout="wide")


st.markdown(
        """
        # Display $PLANET transactions
        """
    )

st.info("""
        If you try to get all transactions from Algoexplorer.io for a given wallet address, you will find a lot of transactions with 0 value.
        It's hard to identify the transactions with real amount of PLANETS.
        Therefore I have created this small web app to solve this issue.
        The webapp uses the Algoexplorer API with parameters like PLANETS asset-id: 27165954 and amount greater than 0.
        """
        )


st.sidebar.write("")
st.sidebar.title("About")
st.sidebar.info(
            """
            The webapp is created by Astr0 to help the PW community and it is ad-free
            and open-source. If you find the app useful you can support me here: 
            Algorand: `3KBG44MVZSKKOUDW7QJ2QS2FYHFIHNTLT3Q7MTQ2CLG65ZHQ6RL6ENZ7GQ`  
                     
            You can find the source and contribute [here](https://github.com/astritm/planetwatch).  
            
            Special thanks to the PW discord mods @feralfether, @inforkill, @Wagner and many more who have actively or passively
            contributed to the project.
            
            If you are not yet aware about PlanetWatch project, please check it here https://planetwatch.io/ 
            Where you can buy different types of Airquality sensor and correspoding licenses.
            Running a sensor and actively sending data streams to planetwatch you will be rewarded with PLANETS tokens.
            """
            )


Total_rx = 0
Total_tx = 0
Diff = 0
Counter_tx=0
Wallet_Address = st.text_input('Please enter a your wallet address without spaces and hit Enter')
if len(Wallet_Address) == 58:

    response = requests.get('https://algoexplorerapi.io/idx2/v2/transactions?address={}&asset-id=27165954&currency-greater-than=0'.format(Wallet_Address)).text
    response_info = json.loads(response)
   
    for transactions in response_info['transactions']:
     amount = transactions['asset-transfer-transaction']['amount']
     amount = amount / 1000000
     amount = round (amount, 2)
     timestamp = transactions['round-time']
     your_date = datetime.fromtimestamp(timestamp)
     Counter_tx = Counter_tx + 1
     if transactions['asset-transfer-transaction']['receiver'] == Wallet_Address:
        Total_rx = amount + Total_rx
        st.write ("Date:" , your_date, "PLANETS: + " , amount, " txid: " , transactions['id'] )
        
     if transactions['asset-transfer-transaction']['receiver'] != Wallet_Address:
        Total_tx = amount + Total_tx
        st.write ("Date:" , your_date , "PLANETS: -", amount, " txid: " , transactions['id'] )
        
    st.write()
  
    Total_rx = round(Total_rx, 2)
    
    
    #st.write ("Total Planets Received: ", (Total_rx))
    #st.write()
    Total_tx = round(Total_tx, 2)
    #st.write ("Total Planets Sent: ", Total_tx)
    #st.write()
    Diff = Total_rx - Total_tx
    Diff = round(Diff, 2)
    #st.write ("Diff: ", Diff)
    #st.write()
    #st.write ("Total Transactions with PLANETS > 0: ", Counter_tx)
    #st.write()
    
    st.write(pd.DataFrame({
    'Total Received': [Total_rx],
    'Total Sent': [Total_tx]
    }))
