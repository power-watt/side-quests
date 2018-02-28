# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:42:49 2018

@author: Jacob Marshall
"""
#from iexfinance import Stock
#from iexfinance import Stock
from iexfinance import get_historical_data
import time
import datetime
import csv

symbols = []
ts = 15 # sample time (seconds)

# Read in stock symbols
with open('symbols.txt', 'r') as csvFile:
    csvObj = csv.reader(csvFile, delimiter='\t')
    for line in csvObj:
        symbols = line




def realTime(n):
    stocks = Stock(symbols)
    for i in range(n):
        prices = stocks.get_price()
        t = datetime.datetime.now()
        print('{} \t {}'.format(t, prices))
        with open('realTime.txt', 'a') as f:
            f.write(str(t))
            for key in prices:
                f.write('\t{}'.format(prices[key]))
            f.write('\n')
        time.sleep(ts)
        
def historical():
    start = datetime.datetime(2017, 2, 9)
    end = datetime.datetime(2017, 5, 24)
    d = get_historical_data(symbols, start=start, end=end, output_format='pandas') #daily open, high, low, close, volumne
#    print(df.head())
#    print(type(df['XOM']))
    print(d)

if __name__  == '__main__': 
    realTime(30)