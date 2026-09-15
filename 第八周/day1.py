with open("第八周\stock_prices.txt", "r", encoding="utf-8") as f:
    content = f.read()
    for i in (content or '').split():
        print(i, type(i))