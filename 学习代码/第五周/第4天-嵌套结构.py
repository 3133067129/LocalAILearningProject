buy_price = 100
present_price = float(input("please input present price:"))
profit_rate = (present_price-buy_price) / buy_price
if profit_rate > 0:
        if profit_rate >= 0.15:
                print("you have reach your stop profit line")
        else:
                print("keep your postion")
else:
        if profit_rate <= -0.07:
                print("you have reach your stop loss line")
        else:
                print("keep your postion")