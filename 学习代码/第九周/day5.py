import numpy as np

# 4 天 × 4 列：open, high, low, close
prices = np.array([
    [100.0, 101.5, 99.8, 100.9],
    [101.0, 102.3, 100.5, 101.8],
    [102.0, 103.0, 101.2, 102.5],
    [101.5, 102.8, 100.9, 102.0]
])

"""
total_close：所有收盘价之和（prices[:, 3].sum()）。

avg_close：收盘价均值。

close_std：收盘价标准差。

highest_high：最高价中的最大值（第 2 列）。

lowest_low：最低价中的最小值（第 3 列）。

avg_per_day：每天 4 个价格的均值（按行，用 axis=1），结果长度 4。

avg_per_column：每列 4 天的均值（按列，用 axis=0），结果长度 4。

daily_range：每天的最高价 − 最低价（第 2 列 − 第 3 列），结果长度 4。
"""

total_close = prices[:, 3].sum()
avg_close = np.mean(prices[:, 3])
close_std = np.std(prices[:, 3])
highest_high = np.amax(prices[:, 1])
lowest_low = np.amin(prices[:, 2])
avg_per_day = np.mean(prices, 1)
avg_per_column = np.mean(prices, 0)
daily_range = np.ptp(prices, 1)
