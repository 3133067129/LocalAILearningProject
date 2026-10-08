import numpy as np
close_prices = np.array([102.5, 103.8, 101.2, 104.6, 105.1, 103.9, 106.3, 107.0, 105.8, 108.2])

daily_returns = np.diff(close_prices) / close_prices[:-1]
mean_return = np.mean(daily_returns)
std_return = np.std(daily_returns) 

"""
改进：
positive_days = np.sum(daily_returns > 0)
原式：
positive_days = len(daily_returns[daily_returns > 0])
"""
positive_days = np.sum(daily_returns > 0)
positive_ratio = positive_days / len(daily_returns)

n = 0
days = 0
a, b = 0, 0
for a in close_prices:
    if a >= b:
        b = a
        n +=1
        if n >= days:
            days = n 
    else: 
        b = a
        n = 0
print(days)
    