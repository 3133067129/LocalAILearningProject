with open("stock_record.txt", 'w', encoding='utf-8') as f:
    stocks = [
        {"code": "AAPL", "price": 189.5, "change": 1.23},
        {"code": "MSFT", "price": 415.2, "change": -0.45},
        {"code": "GOOGL", "price": 152.8, "change": 0.87}
    ]
    print(f.name)
    for stock in stocks:
        f.write(f"代码:{stock['code']} 价格:{stock['price']} 变化:{stock['change']}\n")

with open("stock_record.txt", 'a', encoding='utf-8') as f:
    stock_addition = {"code": "TSLA", "price": 248.4, "change": -2.1}
    f.write(f"代码:{stock_addition['code']} 价格:{stock_addition['price']} 变化:{stock_addition['change']}\n")

with open("stock_record.txt", 'r', encoding='utf-8') as f:
    print(f.read())