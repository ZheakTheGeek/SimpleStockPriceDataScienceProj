import pandas as pd
import streamlit as sl
import yfinance as yf

sl.write("""
# Simple Stock Price App

These are stock closing price and volume of S&P 500 Stocks and Google

""")
#Define ticker symbol and get data on the ticker

#Creates graphics for Charts passed into method
def write_charts(inlist,tickers):
    incrementer = 0
    for i in inlist:
        print(type(i))
        sl.write("""# Closing Price """ + tickers[incrementer])
        sl.line_chart(i.Close)       
        sl.write("""# Volume """ + tickers[incrementer])
        sl.line_chart(i.Volume)
        if sum(i.Dividends) != 0:
            dividends = get_dividends(i.Dividends)
            sl.write("""# Dividends """ + tickers[incrementer])
            sl.line_chart(dividends)
            sl.write(dividends)
            sl.write(type(dividends))
        incrementer +=1       
# Gets Data for list of tickers sent into the method
def get_data(inlist):
    outlist =[]
    for i in inlist:
        outlist.append(yf.Ticker(i))
    return outlist
#Returns Datafiles for history for passed in list
def get_df(data):
    outlist = []
    for i in data:
        outlist.append(i.history(period='1d', start = '2010-5-31',end ='2020-5-31'))
    return outlist

def get_dividends(stock):
    outlist = stock[stock != 0]
    return outlist
              #  stock.Dividends.pop(x)

tickerSymbols = ['BTC-USD','ETH-USD', 'DOGE-USD', 'GOOGL', 'MMM', 'ABT', 'ABBV']
tickerData = get_data(tickerSymbols)
tickerDf = get_df(tickerData)

write_charts(tickerDf,tickerSymbols)