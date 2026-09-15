stocks = [
    {"name": "茅台", "change": 0.02},
    {"name": "宁德时代", "change": -0.01},
    {"name": "BYD", "change": 0.06},
    {"name": "招行", "change": 0.08},
]
for stock in stocks:
        if stock['change'] > 0.05:
                print(f"找到：{stock['name']}")
                # break
        elif stock['change'] < 0:
                continue
print("筛选结束")