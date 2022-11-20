# import pickle
# from pathlib import Path

import streamlit as st # pip install streamlit
import streamlit_authenticator as stauth # pip install streamlit-authenticator
import requests
import pandas as pd # pip install pandas 
from genfunctions import getdata
from deta import Deta # pip install deta

# import plotly.express as px
# import plotly.io as pio
# pio.renderers.default = 'browser'

## --- Displaying raw data ---
# create a data elements and let the reader know the data is loading
data_load_state = st.text('Loading data...')

rawdata = getdata(status = 'active-companies')
indmetrics = rawdata.INDUSTRY.value_counts().reset_index()
indmetrics.columns = ['INDUSTRY NAME', 'NUMBER OF COMPANIES']
#indmetrics = pd.DataFrame(indmetrics)
#st.dataframe(indmetrics)
df = indmetrics.head(5)
#df = px.bar(df, x='INDUSTRY NAME', y='NUMBER OF COMPANIES')
#df.show()
st.title('Fastest growing industries in Dubai Free Zone - DAFZA as of Today')

st.bar_chart(data=df, x='INDUSTRY NAME', y='NUMBER OF COMPANIES')
data_load_state.text('Done!')

st.set_page_config(
        page_title = "DAFZA Analytics",
        page_icon='',
        layout='wide',
        initial_sidebar_state='expanded',
        menu_items={
            'About': ''}
        )
