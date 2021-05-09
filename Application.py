

import pandas as pd
import streamlit as sl
import yfinance as yf

sl.write("""
# Simple Stock Price App

These are stock closing price and volume of S&P 500 Stocks and Google

""")
#Define ticker symbol and get data on the ticker


def write_charts(inlist):
    for i in inlist:
        sl.write(""" 
                 # Closing Price """)
        sl.line_chart(i.Close)
        
        sl.write("""
                 # Volume
                 """)
        sl.line_chart(i.Volume)
    
def get_data(inlist):
    outlist =[]
    for i in inlist:
        outlist.append(yf.Ticker(i))
    return outlist

def get_df(data):
    outlist = []
    for i in data:
        outlist.append(i.history(period='1d', start = '2010-5-31',end ='2020-5-31'))
    return outlist


tickerSymbols = ['GOOGL', 'MMM', 'ABT', 'ABBV']
tickerData = get_data(tickerSymbols)

type(tickerData)

sl.write(type(tickerData))
tickerDf = get_df(tickerData)

write_charts(tickerDf)