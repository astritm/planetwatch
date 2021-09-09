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
from streamlit import metric

def write(state):
 awair_settings = " "
 
 st.markdown(
          """
          <h1 style="color: darkblue; text-align:center;">Aware Elements Dashboard</h1>
         
         
         """, unsafe_allow_html=True
          
          
      )
  
 st.info('Enable API first as expalined in the awair official web [here] (https://support.getawair.com/hc/en-us/articles/360049221014-Awair-Element-Local-API-Feature#h_01F40FBBW5323GBPV7D6XMG4J8). DMZ is also be required to be able to access the Awair IP from the outside world!')
 
 form = st.form(key='form')
 ip = form.text_input('Plesase enter the local IP address of Awair Elements:')
 submit = form.form_submit_button('Submit')
 
 if submit:
  response_awair_aq = requests.get('http://{}/air-data/latest'.format(ip)).text
  r = json.loads(response_awair_aq)
  response_awair_settings = requests.get('http://{}/settings/config/data'.format(ip)).text
  awair_settings = json.loads(response_awair_settings)
  #st.write(r)
  
  score = r['score']
  temp = r['temp']
  humid = r['humid']
  co2 = r['co2']
  voc = r['voc']
  pm25 = r['pm25']
  
  score = str(score) + " %"
  #temp = str(temp) + " °C/°F"
  temp = round(temp, 1)
  humid = round(humid, 1)
  humid = str(humid)+ " %"
  co2 = str(co2) + " ppb"
  voc = str(voc) + " ppm"
  pm25 = str(pm25) + " µg/m³"
  
  st.markdown(' ### AQ DATA')
  st.write('---------------------')
  
  col1, col2, col3 = st.columns(3)
  
  col1.metric("Score", score)
  col2.metric("Temperature", temp)
  col3.metric("Humidity", humid)
  
  col4, col5, col6 = st.columns(3)
  
  col4.metric("CO₂", co2)
  col5.metric("Chemicals", voc)
  col6.metric("pm2.5", pm25)
  st.write('---------------------')
  
  st.markdown("### Air Quality Factors Measured By Awair Element")
  st.write("------------")
  
  with st.expander("Awair Score"):
         st.markdown(
             """
             ## How do I read my Awair Score? What can the Trend Graph view tell me about my air quality?
             Your Awair Score
             The Awair score is a simple, quick way to give you a basic overview of your current air quality. 
             Based on a scale of 0 (extremely poor air quality) to 100 (excellent air quality). 
             This score is calculated from a combination of air quality standards from the EPA and the preferences you set in the Awair app.  
                        
             """)
 
 
  with st.expander("Temperature"):
         st.markdown(
             """
             ## Temperature 
             The temperature index is designed to help you maximize occupant comfort and productivity. 
             Index 1, the optimal index, spans a range of 17-26°C (63-79°F), and ideally 18-25°C (64-77°F). 
             An indoor temperature above this range can lead to overheating, dehydration, and exhaustion, while far below this range may lead to dry air, a weakened immune system, and overall discomfort. 
             Aware included the lower temperatures for customers that find colder temperatures more comfortable and energizing and also ideal for better sleep. 
             Temperature can seem like one of the more subjective air factors; however, it is important to note that temperature does have a real effect on human health, and directly impacts other factors, such as the volatility of VOCs and the relative humidity.
                        
             """)
         
  with st.expander("Hmidity"):
         st.markdown(
             """
             ## Relative Humidity
             Relative humidity has a significant impact on comfort, respiratory health, and productivity. Humidity levels between 40~60% are considered healthy, but ideally between 40~50% for peak indoor performance. 
             This range is recommended especially for those with allergies, asthma, or other respiratory illnesses. Keeping humidity below the upper end of the spectrum can minimize the growth, spread, and survival of mold, viruses, and bacteria. 
             Alternatively, dry air can lead to respiratory issues and the increased likelihood of viral transmission.
                        
             """)
  with st.expander("Carbon Dioxide (CO₂)"):
         st.markdown(
             """
             ## Carbon Dioxide (CO₂)
             Carbon Dioxide (CO₂) is an important consideration when it comes to comfort and productivity. Air with high levels of CO₂ can lead to difficulty concentrating, decreased cognitive ability, and fatigue. 
             It's important to use monitors to measure carbon dioxide because due to higher levels' affects on our cognitive abilities, it can be easy to miss the early warning signs of fatigue. 
             Typically, CO₂ levels outdoors are around 400 parts per million (ppm), thus the lowest level achievable indoors is around 400 ppm. 
             Concentrations well below 1000 ppm are considered good, but below 500~600 ppm is ideal for a healthy and productive workspace.
                        
             """)
         
  with st.expander("Chemicals (TVOCs)"):
         st.markdown(
             """
             ## Chemicals (TVOCs)
             Total Volatile Organic Compounds (TVOCs) are a diverse group of chemicals that are commonly found in the air in homes and offices. 
             They are both naturally occurring and man-made. TVOCs can be found in many manufactured goods as well as common cleaners, paint, carpeting, upholstery, sealants, and pressed wood. Unlike other chemicals in the air, TVOCs are generally measured as a cohesive group because of their cumulative effect on health and comfort. 
             When many different VOCs accumulate in a closed environment, they can interact to form new VOCs or glom together to even form Fine Dust (PM2.5) particles.
             TVOCs can lead to a wide range of health effects. Moderate levels of exposure can cause headaches, fatigue, allergic skin reactions, eye and throat irritation, and other symptoms that can affect comfort, concentration, and productivity. Higher concentrations have been associated with more severe health consequences such as cognitive impairment, overworked liver and kidneys, and even cancer. It’s important to try to minimize the amount of TVOCs in your environment and maintain levels well below 1,000 parts per billion (ppb) or 1 ppm, but ideally below 100~333 ppb.
                        
             """)
         
  with st.expander("Fine Dust (PM2.5)"):
         st.markdown(
             """
             ## Fine Dust (PM2.5)
             There are two groups of particulate matter that have garnered the most attention: PM2.5 and PM10. PM2.5 is any particulate matter that is 2.5 microns in width or smaller, while PM10 is any particulate matter that is 10 microns in width or smaller. 
             Fine dust is a primary trigger for allergy and asthma attacks, as well as eczema flare-ups. It can worsen the symptoms of chronic and acute bronchitis as well as heart and lung disease.
             Particles that are 2.5 microns in width are of more concern because they are able to permeate membranous tissue and travel deep into the respiratory tract and bloodstream, causing short-term irritation and potential long-term health effects, including respiratory problems, heart disease, and cancer. 
             Alternatively, particles that are 10 microns in width primarily irritate the upper respiratory tract, aggravating allergies and asthma, and cause other health concerns. While both PM2.5 and PM10 have a negative impact on your health, PM2.5 can stay suspended in the air for a much longer period and can cause more severe health effects in the long-term.
             Keeping fine dust to an absolute minimum is essential for health reasons; however, try to maintain PM2.5 levels well below 35 micrograms per cubic meter (µg/m³), and ideally below 12~15 µg/m³.
             """)
        
         
         
 
  st.markdown("### Deivce Info")
  st.write("----------")
  st.write(awair_settings)
