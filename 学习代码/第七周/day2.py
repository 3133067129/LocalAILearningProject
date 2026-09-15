def calc_return(price_buy, price_sell):
        return (price_sell - price_buy) / price_buy

price_buy, price_sell = 100, 105.5
print(f"持有期收益率：{calc_return(price_buy, price_sell):.2%}")
