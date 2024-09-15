# Stock tracker for the last 5 trading days
import requests
import numpy as np
import os
from dotenv import load_dotenv
from datetime import datetime as dt

load_dotenv() # take API key from .env file

API_KEY = os.getenv('API_KEY')
SYMBOL = "AAPL"

# intraday fetches the stock data every hour of tbe trading day
daily_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={SYMBOL}&outputsize=compact&apikey={API_KEY}"
hourly_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&month=2024-09&interval=60min&apikey={API_KEY}"
daily_response = requests.get(daily_url).json()
hourly_response = requests.get(hourly_url).json()

print(daily_response["Meta Data"]["2. Symbol"])

# daily stock information
time_series_daily = daily_response["Time Series (Daily)"]
dates_list = list(time_series_daily.keys())

# hourly stock information
time_series_hourly = hourly_response["Time Series (60min)"]
hourly_list = list(time_series_hourly.keys())
print(hourly_list)
# financial data for the last 5 trading days
for date in dates_list[:1]:
    print(date)
    print(f"Open: {time_series_daily[date]['1. open']}")
    print(f"High: {time_series_daily[date]['2. high']}")
    print(f"Low: {time_series_daily[date]['3. low']}")
    print(f"Hourly Data")
