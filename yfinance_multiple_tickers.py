import yfinance as yf
import datetime
import pandas as pd

stocks = ["AMZN", "MSFT", "INTC", "GOOD", "INFY.NS"]
start = datetime.datetime.today()-datetime.timedelta(30)
end = datetime.datetime.today()
cl_price = pd.DataFrame()

ohlcv_data = {}

for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)["Adj Close"]
    
for ticker in stocks:
    ohlcv_data[ticker] = yf.download(ticker, start, end)
    
print(ohlcv_data["MSFT"]["Open"])