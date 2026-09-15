def calc_net_return(buy_price, sell_price, fee_rate=0.001):
        return (sell_price - buy_price) / buy_price - 2 * fee_rate

print(f"{calc_net_return(100, 105.5):.2%}")
print(f"{calc_net_return(100, 105.5, fee_rate=0.003):.2%}")