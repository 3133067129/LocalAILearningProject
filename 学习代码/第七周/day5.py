stocks = [
    {"code": "AAPL", "return": 0.055},
    {"code": "TSLA", "return": -0.02},
    {"code": "MSFT", "return": 0.031},
]
new = sorted(stocks, key=lambda s:s['return'], reverse=True)
for i in new:
        print(f"{i['code']}:{i['return']:.2%}")
