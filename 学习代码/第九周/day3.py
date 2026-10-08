import numpy as np

closes = np.array([10.2, 10.5, 10.3, 11.0, 10.8, 11.2, 11.5])

prices = np.array([
    [100.0, 101.5, 99.8, 100.9],
    [101.0, 102.3, 100.5, 101.8],
    [102.0, 103.0, 101.2, 102.5],
    [101.5, 102.8, 100.9, 102.0]
])

first_three = closes[:3]
last_two = closes[5:]
every_other = closes[::2]
reversed_closes = closes[::-1]
middle_days = closes[2:5]


second_day = prices[1,...]
close_prices = prices[...,3]
first3_open_close = prices[0:3,...][...,[0,3]]
last_day_high_low = prices[3,[1,2]]

