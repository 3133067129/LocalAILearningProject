def calc_return(buy_price, sell_price):
        return (sell_price - buy_price) / buy_price

def calc_net_return(buy_price, sell_price, fee_rate=0.001):
        return (sell_price - buy_price) / buy_price - 2 * fee_rate

def summarize(returns):
        return max(returns), min(returns), sum(returns)/len(returns)

def rank_stocks(stocks):
        return sorted(stocks, key=lambda s:s['return'], reverse=True)

stocks = [
    {"code": "AAPL", "buy": 100, "sell": 105.5},
    {"code": "TSLA", "buy": 200, "sell": 196},
    {"code": "MSFT", "buy": 300, "sell": 309},
]

returns = []
for stock in stocks:
        returns.append(calc_net_return(stock['buy'], stock['sell']))
        stock["return"] = calc_net_return(stock['buy'], stock['sell'])

max, min, avg = summarize(returns)


print(f"最小收益率：{min:.2%}")
print(f"最大收益率：{max:.2%}")
print(f"平均收益率：{avg:.2%}")

for stock in rank_stocks(stocks):
        print(f"{stock['code']}: {stock['return']:.2%}")
