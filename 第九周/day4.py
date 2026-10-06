import numpy as np

# 某股票 10 个交易日的收盘价与成交量（百万股）
closes = np.array([10.2, 10.5, 10.3, 11.0, 10.8, 11.2, 11.5, 11.1, 10.9, 12.0])
volumes = np.array([2.1, 1.8, 2.5, 3.2, 2.0, 4.1, 3.8, 2.9, 1.5, 5.2])

above_11 = closes[closes > 11]
high_volume = volumes[volumes > 3]
price_and_volume = closes[(closes > 11) & (volumes > 3)]
not_high_volume = closes[~(volumes > 3)]
above_mean_close = closes[closes > np.mean(closes)]





print(not_high_volume) 