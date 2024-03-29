import streamlit as st
from streamlit.elements import layouts
import streamlit_analytics

st.set_page_config(page_title="PW Tool", layout="wide")

# Load pages
#import transactions
import export_data
import calculator
#import awair_cloud

import FAQ



PAGE_NAMES = ["Export Transaction Data", "Planets Calculator", "FAQ"]
PAGE_SRCS = [export_data, calculator, FAQ]



@st.cache(allow_output_mutation=True)
def storage():
 return  []

state = storage()


def main():

   if len(state) == 0:
    state.extend([0., 0., 0.])
        
   with streamlit_analytics.track():
    
    st.sidebar.image("https://www.planetwatch.io/wp-content/themes/Planetwatchre/images/PlanetWatch_logo_new-2.png", width=200)
    page_selection = st.sidebar.radio("Menu", PAGE_NAMES)
    page_selection_ix = PAGE_NAMES.index(page_selection)
    page = PAGE_SRCS[page_selection_ix]

    page.write(state)


    st.sidebar.title(" About ")

    st.sidebar.info(
        """
                    
        The webapp is created by Astr0 to help the PW community and it is ad-free
        and open-source. 
        
        If you find the app useful you can support me in the 
        Algorand wallet address below:
        """
        )
    st.sidebar.write('We love ALGOS or PLANETS :)')
    st.sidebar.image("data:image/gif;base64,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", width=120)
    st.sidebar.info(
        """           
        Thanks to **Chris Crypto Coffee** for making such a lovely instructional and informative videos about PlanetWatch in general.
        Please check his channel in the following link:
        https://bit.ly/2WNAwxk
        
        If you are not yet aware about PlanetWatch project, please check it here https://planetwatch.io/ 
        Where you can buy different types of Airquality sensor and correspoding licenses.
        Running a sensor and actively sending data streams to planetwatch you will be rewarded with PLANETS tokens.
        """
        )



if __name__ == "__main__":
    main()
