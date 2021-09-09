import streamlit as st
from streamlit.elements import layouts
import streamlit_analytics

# Load pages
import transactions
import calculator
import aware



PAGE_NAMES = ["Transaction Viewer", "Aware Dashboard", "Planets Calculator"]
PAGE_SRCS = [transactions, aware, calculator]

st.set_page_config(page_title="PW tools")

@st.cache(allow_output_mutation=True)
def storage():
 return  []

state = storage()


def main():

    if len(state) == 0:
        state.extend([0., 0., 0.])
    
    with streamlit_analytics.track():


        st.sidebar.image('https://mlawiy0je0ms.i.optimole.com/206F41w.AtuS~2d373/w:100/h:auto/q:auto/https://www.planetwatch.io/wp-content/themes/Planetwatchre/images/PlanetWatch_logo_new-2.png', width=200)
        page_selection = st.sidebar.radio("Menu", PAGE_NAMES)
        page_selection_ix = PAGE_NAMES.index(page_selection)
        page = PAGE_SRCS[page_selection_ix]
        
        page.write(state)
        
        
        st.sidebar.title("*** About ***")
        
        st.sidebar.info(
            """
                       
            The webapp is created by Astr0 to help the PW community and it is ad-free
            and open-source. 
            
            If you find the app useful you can support me in the 
            Algorand wallet address below:
            ##### 3KBG44MVZSKKOUDW7QJ2QS2FYHFI HNTLT3Q7MTQ2CLG65ZHQ6RL6ENZ7GQ
                    
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



if __name__ == "__main__":
    main()
