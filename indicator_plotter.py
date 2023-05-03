import pandas as pd
import requests
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import io
from scipy.signal import hilbert
import sys
import datetime as dt

symbol = 'AAPL'  # Replace with the stock symbol of your choice
#api_key = 'GETFNQ5SDYN8OV2N'  # Replace with your Alpha Vantage API key
#url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}&datatype=csv'
start_date = dt.datetime.now() - dt.timedelta(days=1)
end_date = dt.datetime.now()
data = yf.download(symbol, start=start_date, end=end_date, interval='1m')

#response = requests.get(url)
#data = pd.read_csv(io.StringIO(response.content.decode('utf-8')))

# Calculate Ehlers' Hilbert Sine Wave
analytic_signal = hilbert(data['Close'])
hilbert_sine_wave = np.imag(analytic_signal)

# Calculate momentum indicator based off buying and selling volume
volume = data['Volume']
buying_pressure = np.where(data['Close'] > data['Open'], volume, 0)
selling_pressure = np.where(data['Close'] < data['Open'], volume, 0)
momentum = pd.Series(buying_pressure - selling_pressure).rolling(window=10).mean()

# Calculate Pro/Am indicator based off average trade size
trade_size = data['Adj Close'] * data['Volume']
trade_size_diff = trade_size.diff()
pro_am = trade_size_diff.rolling(window=10).sum() / volume.rolling(window=10).sum()

# Plot Ehlers' Hilbert Sine Wave
plt.plot(data.index, hilbert_sine_wave, label="Ehlers' Hilbert Sine Wave")

# Plot momentum indicator
plt.plot(data.index, momentum, label='Momentum Indicator')

# Plot Pro/Am indicator
plt.plot(data.index, pro_am, label='Pro/Am Indicator')

# Set the title and axis labels
plt.title(f'{symbol} Stock Indicators')
plt.xlabel('Time')
plt.ylabel('Value')

# Add a legend to the plot
plt.legend()

# Show the plot
plt.show()
