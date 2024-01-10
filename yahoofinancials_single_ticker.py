# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 12:45:46 2023

@author: surya
"""

from yahoofinancials import YahooFinancials

ticker = 'MSFT'
yahoo_financials = YahooFinancials(ticker)
data = yahoo_financials.get_historical_price_data("2018-04-24", "2020-04-24", "daily")