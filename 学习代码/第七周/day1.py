def calc_return(price_buy, price_sell):
        """计算持有期收益率"""
        profit_rate = (price_sell - price_buy) / price_buy
        return profit_rate

price_buy, price_sell = 100, 110
print(f"持有期收益率：{calc_return(price_sell = price_sell, price_buy = price_buy):.2%}")


