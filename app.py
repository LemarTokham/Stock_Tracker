# Stock tracker for the last 5 trading days
import requests
import numpy as np
import os
from dotenv import load_dotenv
from datetime import datetime as dt

load_dotenv() # take API key from .env file

API_KEY = os.getenv('API_KEY')
print(f"my API key is {API_KEY}")
SYMBOL = "AAPL"

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={SYMBOL}&outputsize=compact&apikey={API_KEY}"

response = requests.get(url).json()

print(response["Meta Data"]["2. Symbol"])
time_series = response["Time Series (Daily)"]
dates_list = list(time_series.keys())
print(dates_list)
# financial data for the last 5 trading days
for date in dates_list[:5]:
    print(date)
    print(f"Open: {time_series[date]['1. open']}")
    print(f"High: {time_series[date]['2. high']}")
    print(f"Low: {time_series[date]['3. low']}")
