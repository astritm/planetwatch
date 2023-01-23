import streamlit as st


def write(state):
 st.markdown(
          """
          <h2 style="color: darkblue; text-align:center;">Planetwatch FAQ</h2>
          
          ------------
          
          """, unsafe_allow_html=True
          
          
          
      )
 
 with st.expander("I. Type 1 sensor - outdoor"):
  st.markdown( """
              <html style="color: #3ED625; text-align:left;">Q1. How can I buy a Type one sensor (Airqino)</html>
              A1. First you have to buy a Type 1 license at planetwatch <html><a href="https://www.planetwatch.io/pick-your-license/">website</a> </html>.
                  They will put you in the queue basted on the licenses sold and number of sensors available for the next batches.
                  For EU users payment is done only in PLANETS for the sensor and for the license.
                  You will be notified from the planetwatch team when you are available to purchanse the sensor.
                  
             ---
             
              <html style="color: #3ED625; text-align:left;">Q1. How much does Type 1 sensor costs?</html>
              A2. Type 1 (Airqino) costs €1,350.00 (VAT excluded). Payment should be done in PLANETS.
                 
             
             ---
             
              <html style="color: #3ED625; text-align:left;">Q3. How do I know if ther are Type 1 sensors in my area?</html>
              A3. Go to the planetwatch <html><a href="https://map.planetwatch.io/map/">map</a></html>
                  At search place box type your address.
                  You will see the area with rectangles (they are 0.72km2).
                  If one of the rectangles has a color, click there and scroll down on the page on the left.
                  At the botom of that page you will see the sensor Type.
                  It means the cell already have a sensor.  
             
             ---
              <html style="color: #3ED625; text-align:left;">Q4. How can I activate my Airqino when it's delivered?</html>
              A4. Check the feralfether step by step reddit guid <html><a href="https://www.reddit.com/r/PlanetWatchers/comments/o9k96k/type_1_sensor_airquino_first_setup/">Airquino - First Setup</a></html>                                  
             
              
              """, unsafe_allow_html=True
              )
  
 with st.expander("II. Type 2 sensor - outdoor"):
  st.markdown( """
              <html style="color: #3ED625; text-align:left;">Q1. How can I buy a Type 2 sensor?</html>
                  A1. First you have to buy a Type 1 license at planetwatch <html><a href="https://www.planetwatch.io/pick-your-license/">website</a> </html>.
                  They will put you in the queue basted on the licenses sold and number of sensors available for the next batches.
                  For EU users payment is done only in PLANETS for the sensor and for the license.
                  You will be notified from the planetwatch team when you are available to purchanse the sensor.
                  
                  
             ---
             
              <html style="color: #3ED625; text-align:left;">Q2. Is there a Type 2 sensor currently available in the market?</html>
              A2. NO!
                  Not at the time of writing this Q&A.
             
             ---
             
              <html style="color: #3ED625; text-align:left;">Q3. How do I know if ther are Type 2 sensors in my area?</html>
              A3. Go to the planetwatch <html><a href="https://map.planetwatch.io/map/">map</a></html>
                  At search place box type your address.
                  You will see the area with rectangles (they are 0.72km2).
                  If one of the rectangles has a color, click there and scroll down on the page on the left.
                  At the botom of that page you will see the sensor Type.
                  It means the cell already have a sensor.            
             ---                                  
             
              
              """, unsafe_allow_html=True
              )
  
 with st.expander("III. Type 3 sensor - indoor (Premium)"):
   st.markdown( """
              <html style="color: #3ED625; text-align:left;">Q1. How can I buy a Type3 sensor?</html>
                  A1. First you have to buy a Type 3 license at planetwatch <html><a href="https://www.planetwatch.io/pick-your-license/">website</a> </html>.
                  They will put you in the queue basted on the licenses sold and number of sensors available for the next batches.
                  For EU users payment is done only in PLANETS for the sensor and for the license.
                  You will be notified from the planetwatch team when you are available to purchanse the sensor.
                  
             
             ---
             
              <html style="color: #3ED625; text-align:left;">Q3. Can I have Type3 and Type4 at my home (same location)?</html>
              A1. Yes!
                  You can have in the same location different types of sensors, one per type. 
             
             ---                                  
             
              
              """, unsafe_allow_html=True
              )
  
 with st.expander("IV. Type 4 sensor - indoor"):
   st.markdown( """
              <html style="color: #3ED625; text-align:left;">Q1. Can I have more than one T4 sensor at my home?</html>
              A1. No, only one Type per household is allowed. 
                  The execpeption being with Atmotube Pro which has to be away from the same location for 30 percent of the time!
                  
             ---
             
              <html style="color: #3ED625; text-align:left;">Q2. Should I buy the license first to get in queue for the sensor?</html>
              A2. You can buy the Type4 sensor without buying the license firts.
                  As the time of writing this answer, there are two qualified products as Planetwatch T4 sensors Awair Elements and Atmotube Pro!
             
             ---
             
              <html style="color: #3ED625; text-align:left;">Q3. Can I have more than one T4 sensor at my home?</html>
              A3. No, only one Type per household is allowed. 
                  The execpeption being with Atmotube Pro which has to be away from the same location for 30 percent of the time
             
             ---                                  
             
             <html style="color: #3ED625; text-align:left;">Q4. Is the new Type 4 device going to be able to connect directly to PlanetWatch servers or does it need to connect to a PlanetWatch App from a smartphone?</html>
            A4. No, it will not need to be connected to the smartphone. 
             
                        
             
              
              """, unsafe_allow_html=True
              )
  
 with st.expander("V. Licenses related"):
   st.markdown( """
              <html style="color: #3ED625; text-align:left;">Q1. Can I use 1 license for two sensors?</html>
              A1. NO! 
                  One license per sensor.
                  
             ---
             
              <html style="color: #3ED625; text-align:left;">Q2. Do I need to have different emails address for buying more than one license?</html>
              A2. NO!
                  You can buy as much licenses as you want with your single email address.
                  
             ---
             
              <html style="color: #3ED625; text-align:left;">Q3. Is there a coupon code for licenses?</html>
              A3. Not at the time writing this Q&A.
              
             
             ---                                  
             
              
              """, unsafe_allow_html=True
              )
   
 with st.expander("V. PLANETS Token"):
   st.markdown( """
              <html style="color: #3ED625; text-align:left;">Q1. On which exchange can I buy PLANETS?</html>
              A1. At the time of writing this Q&A only in <html><a href="https://bitfinex.com/?refcode=xuaIhzgt0">Bitfinex</a></html>
                  It will be in Bitmart and Emirex sooner.
                  
             ---
             
              <html style="color: #3ED625; text-align:left;">Q2. What wallet should I use for PLANETS token?</html>
              A2. Algorand wallet (mobile app)
                  Algosigner (chrome extension)
             
              
              """, unsafe_allow_html=True
              )
   
 with st.expander("VI. Other related questions"):
    st.markdown( """
              <html style="color: #3ED625; text-align:left;">Q1. Are there videos, instructions about planetwatch project?</html>
              A1. Yes, you can subscriber to  Chris Crypto Coffee YoutTube <html><a href="https://www.youtube.com/channel/UCDHHM5NoBmGGN3WnBCc_C5A">channel</a></html> for amazing and informative videos.
                  
                  
             ---
              
              """, unsafe_allow_html=True
              )
 
 
