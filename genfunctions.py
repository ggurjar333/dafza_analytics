import pandas as pd
import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def getdata(status):
    configure()
    """Return the dataframe of response json of a URL"""
    datarequest = f'https://companies-in-dubai-free-zones.p.rapidapi.com/{status}'
    headers = {
    "X-RapidAPI-Key": os.getenv('api_key'),
    "X-RapidAPI-Host": "companies-in-dubai-free-zones.p.rapidapi.com"
}
    
    response = requests.request("GET",url=datarequest, headers=headers)
    return pd.read_json(response.json()).transpose()

