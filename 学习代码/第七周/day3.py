def calc_stock_return(buy_price, sell_price, shares):
        return_rate = (sell_price - buy_price) / buy_price
        total_profit = (sell_price - buy_price) * shares
        return return_rate, total_profit
Return_rate, Total_profit = calc_stock_return(100, 105.5, 200)
print(f"Return rate:{Return_rate:.2%} \nTotal profit:{Total_profit:.2f}")