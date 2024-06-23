import requests
import pandas as pd
from ta.momentum import RSIIndicator

def get_klines(symbol='SOLUSDT', interval='1h', limit=200):
    url = f"https://api.bybit.com/v2/public/kline/list?symbol={symbol}&interval={interval}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['result'])
    df['timestamp'] = pd.to_datetime(df['open_time'], unit='s')
    return df

def calculate_rsi(df, period=14):
    rsi = RSIIndicator(df['close'], window=period)
    df['rsi'] = rsi.rsi()
    return df
