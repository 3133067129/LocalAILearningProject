portfolio = [
    {"name": "茅台", "shares": 10, "price": 1850},
    {"name": "宁德时代", "shares": 50, "price": 195},
    {"name": "BYD", "shares": 30, "price": 260},
]
total = 0
for i in portfolio:
        total_price = i['shares'] * i['price']
        print(f"{i['name']} 市值{total_price}")
        total += total_price
print(total)