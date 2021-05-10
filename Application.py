import pandas as pd
import streamlit as sl
import yfinance as yf

sl.write("""
# Simple Stock Price App

Rebuilding of Stock predictive bot, example stocks

""")
#Define ticker symbol and get data on the ticker

#Creates graphics for Charts passed into method
def write_charts(inlist,tickers):
    incrementer = 0
    for i in inlist:
        sl.write("""# """ + tickers[incrementer])
        sl.write("""### Closing Price """)
        sl.line_chart(i.Close)       
        sl.write("""### Volume """)
        sl.line_chart(i.Volume)
        if sum(i.Dividends) != 0:
            dividends = get_dividends(i.Dividends)
            ri = get_relative_increase(dividends)
            sl.write("""### Dividends """)
            sl.line_chart(dividends)
           #  sl.write(""" ### The average increase is """ + str(round((sum(dividends)/len(dividends))*100,2))+'%')
            sl.write(""" ### Non Zero payouts have been listed in the below chart (cents per stock owned)""")
            sl.write(dividends)
            sl.write(""" ### Relative Increase of : """ + str(ri))
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
              
    # TODO - Remove infinity values that occour as a result of division by 0, or of N and O being equal. 
def get_relative_increase(inlist):
    outlist = []
    for i in range(0,len(inlist)-1):
        outlist.append((inlist[i+1]-i)/i)
    return outlist

tickerSymbols = ['BTC-USD','ETH-USD', 'DOGE-USD', 'GOOGL', 'MMM', 'ABT', 'ABBV', 'NSRGY','MSFT', 'JNJ','HSY']
tickerData = get_data(tickerSymbols)
tickerDf = get_df(tickerData)

write_charts(tickerDf,tickerSymbols)