import pandas as pd
import yfinance as yf 
import matplotlib.pyplot as plt

symbol = "600519.SS"
start_date = "2022-01-01"
end_date = "2025-01-01"

data = yf.download(symbol, start=start_date, end=end_date)

data['MA_50'] = data['Close'].rolling(window=50).mean()
data['MA_200'] = data['Close'].rolling(window=200).mean()

data['Signal'] = 0
data['Signal'][data['MA_50'] > data['MA_200']] = 1
data['Signal'][data['MA_50'] < data['MA_200']] = -1

plt.figure(figsize=(20,6))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['MA_50'], label='50-day Moving Average')
plt.plot(data['MA_200'], label='200-day Moving Average')

"""以下这段代码语法更新了，现在已经不能用了"""
plt.scatter(data[data['Signal'] == 1].index, data[data['Signal'] == 1]['MA_50'], marker='^', color='g', label='Buy Signal')
plt.scatter(data[data['Signal'] == -1].index, data[data['Signal'] == -1]['MA_50'], marker='v', color='r', label='Sell Signal')

# plt.scatter(data[data['Signal'] == 1].index, data[data['Signal'] == 1]['MA_50'], marker='^', color='g', label='Buy Signal')
# plt.scatter(data[data['Signal'] == -1].index, data[data['Signal'] == -1]['MA_50'], marker='v', color='r', label='Sell Signal')


plt.title 
plt.legend()
plt.show()