# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 13:05:42 2023

@author: surya
"""
import constants
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time

api_key = constants.api_key

# ts = TimeSeries(key=api_key, output_format='pandas')
# data = ts.get_daily(symbol="EURUSD", outputsize='full')[0]
# data.columns = ['open', 'high', 'low', 'close', 'volume']

all_tickers = ['AAPL', 'MSFT', 'CSCO', 'AMZN', 'GOOG', 'FB']
close_prices = pd.DataFrame()
api_call_count = 0
for ticker in all_tickers:
    start_time = time.time()
    ts = TimeSeries(key=api_key, output_format='pandas')
    data = ts.get_intraday(symbol=ticker, interval='1min', outputsize='full')[0]
    api_call_count += 1
    data.columns = ['open', 'high', 'low', 'close', 'volume']
    data = data.iloc[::-1]
    close_prices[ticker] = data['close']
    if api_call_count==5:
        api_call_count = 0
        time.sleep(60-(time.time() - start_time))