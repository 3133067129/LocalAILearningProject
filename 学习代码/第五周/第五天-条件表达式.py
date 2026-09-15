buy_price = 100
present_price = 101
profit_rate = (present_price - buy_price) / buy_price

status = '止盈' if profit_rate > 0.15 else '止损' if profit_rate < -0.07 else '持有'

print(status)