import time
import yfinance as yf
import pandas as pd 
import matplotlib.pyplot as plt

symbol = '600519.SS'
start_data = '2022-01-01'
end_data = '2023-01-01'

for i in range(3):
    data = yf.download(
        symbol, 
        start = start_data, 
        end = end_data, 
        progress=False,
        threads=False 
        )
    if not data.empty:
        break
    print(f"NO.{i} download error, waiting retry...")
    time.sleep(600)

if data is None or data.empty:
    raise SystemExit("download error, exit project")


data['Signal'] = 0

data['Daily_Return'] = data['Close'].pct_change()

data.loc[data['Daily_Return'] > 0, 'Signal'] = 1

data['Strategy_Return'] = data['Signal'].shift(1) * data['Daily_Return']

data['Cumulative_Return'] = (1 + data['Strategy_Return']).cumprod()

plt.figure(figsize=(10,6))
plt.plot(data['Cumulative_Return'], label='Strategy Cumulative Return', color='b')
plt.plot(data['Close'] / data['Close'].iloc[0], label='Stock Cumulative Return', color='g')
plt.title("Caumulative Return of Strategy vs. Stock")
plt.xlabel("Date")
plt.ylabel("Cumulatice Return")
plt.legend()
plt.show()