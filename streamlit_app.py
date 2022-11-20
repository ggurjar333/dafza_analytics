# import pickle
# from pathlib import Path
#!pip install streamlit-authenticator deta
import streamlit as st # pip install streamlit
# import streamlit_authenticator as stauth # pip install streamlit-authenticator
import requests
import pandas as pd # pip install pandas 
# from genfunctions import getdata
from deta import Deta # pip install deta

# import plotly.express as px
# import plotly.io as pio
# pio.renderers.default = 'browser'

# Generic functions

def getdata(status):
#    configure()
    """Return the dataframe of response json of a URL"""
    datarequest = f'https://companies-in-dubai-free-zones.p.rapidapi.com/{status}'
    headers = {
#    "X-RapidAPI-Key": os.getenv('api_key'),
    "X-RapidAPI-Key": st.secrets['api_key'],
    "X-RapidAPI-Host": "companies-in-dubai-free-zones.p.rapidapi.com"
}
    
    response = requests.request("GET",url=datarequest, headers=headers)
    return pd.read_json(response.json()).transpose()


st.set_page_config(
        page_title="Home"
        )

st.write("# Welcome to Free Zone - Analytics! ")
st.sidebar.success("Select your analytics.")
st.markdown(
        """
        Free Zone - Analytics is an online analytics tool built specifically for
        Free Zone based companies and industries.
        ** Select various analytics from the sidebar** to see some examples of 
        what analytical insights you can see!
        ### What to learn more?
        - Check out [Data APIs](https://rapidapi.com/ggurjar333-Ihcu1gvzM24/api/companies-in-dubai-free-zones)
        - Ask a question on my [LinkedIn](https://www.linkedin.com/in/ggurjarsocl/)
        - Read my other articles on [Data Engineering](https://gauravgurjar.medium.com/)
        """
        )
## --- Displaying raw data ---
# create a data elements and let the reader know the data is loading
data_load_state = st.text('Loading data...')
try:
    rawdata = getdata(status = 'active-companies')
    countries = st.multiselect(
            "Choose countries", ['United Arab Emirates'])
    if not countries:
        st.error("Please select at least one country.")
    else:
        indmetrics = rawdata.INDUSTRY.value_counts().reset_index()
        indmetrics.columns = ['INDUSTRY NAME', 'NUMBER OF COMPANIES']
#indmetrics = pd.DataFrame(indmetrics)
#st.dataframe(indmetrics)
        df = indmetrics.head(5)
#df = px.bar(df, x='INDUSTRY NAME', y='NUMBER OF COMPANIES')
#df.show()
        st.title('Fastest growing industries in Dubai Free Zone - DAFZA as of Today')

        st.bar_chart(data=df, x='INDUSTRY NAME', y='NUMBER OF COMPANIES')
        data_load_stat.text('Done!')

except:
    pass
