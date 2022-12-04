import json
from typing import Counter
import requests
from datetime import datetime
import time
Total_rx = 0
Total_tx = 0
Diff = 0
counter_tx=0
wallet_address = input("Please enter a your wallet address without spaces:\n")
if len(wallet_address) != 58:
 print()
 print ("Not a valid Algorand wallet address!!!")
 print()
 exit()
response = requests.get('https://algoindexer.algoexplorerapi.io/v2/transactions?asset-id=27165954&currency-greater-than=0&address={}'.format(wallet_address)).text
response_info = json.loads(response)

for transactions in response_info['transactions']:
  amount = transactions['asset-transfer-transaction']['amount']
  amount = amount / 1000000
  amount = round (amount, 2)
  timestamp = transactions['round-time']
  your_date = datetime.fromtimestamp(timestamp)
  counter_tx = counter_tx + 1
  if transactions['asset-transfer-transaction']['receiver'] == wallet_address:
    Total_rx = amount + Total_rx
    print ("TX_ID: " , transactions['id'], " Date: ", your_date, " Planets: + " , amount )
  if transactions['asset-transfer-transaction']['receiver'] != wallet_address:
    Total_tx = amount + Total_tx
    print ("TX_ID: " , transactions['id'], " Date: ", your_date, " Planets: - " , amount )
print()
print("====================================")
Total_rx = round(Total_rx, 2)
print ("Total Planets Received: {}".format(Total_rx))
print()
Total_tx = round(Total_tx, 2)
print ("Total Planets Sent:     {}".format(Total_tx))
print()
Diff = Total_rx - Total_tx
Diff = round(Diff, 2)
print ("Diff: {}".format(Diff))
print()
print ("Total Transactions with PLANETS > 0: {}".format(counter_tx))
print()
