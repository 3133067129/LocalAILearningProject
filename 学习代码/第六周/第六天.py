stocks = [
    {"name": "茅台", "buy": 1800, "price": 1850},
    {"name": "宁德时代", "buy": 200, "price": 195},
    {"name": "BYD", "buy": 250, "price": 260},
    {"name": "招行", "buy": 40, "price": 43},
    {"name": "平安", "buy": 50, "price": 48},
]
threshold = 0.02
n = 0
for stock in stocks:
        rate = (stock['price'] - stock['buy']) / stock['buy']
        if rate > threshold:
                print(f"{stock['name']}入选，涨幅 {rate:.2%}")
                n += 1
        elif rate < 0:
                continue
        else: print(f"{stock['name']} 观察")
print(f"共选出{n}只")

Found = False
i = 1
while i <= len(stocks):
        stock = stocks[-i]
        rate = (stock['price'] - stock['buy']) / stock['buy']
        if rate > threshold:
                Found = True
                break
        i += 1
if Found:
        print(f"从后往前第一只是：{stocks[-i]['name']}")
else: print("没有股票达标")
