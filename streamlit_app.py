import streamlit as st
import requests
import pandas as pd
from genfunctions import getdata
#import creds

# url = "https://companies-in-dubai-free-zones.p.rapidapi.com/active-companies"

# headers = {
#    "X-RapidAPI-Key": "c96ec9e4cfmsh0ef4891833a225ap1df1bajsndc1262d5c54a",
#    "X-RapidAPI-Host": "companies-in-dubai-free-zones.p.rapidapi.com"
#}

#rawdata = getdata(datarequest=url, headers=headers)
#print(rawdata)

def main():
    rawdata = getdata(status = 'active-companies')
    print(rawdata)

main()
