# - [ ] **第6天：条件判断综合练习**
# - 练习：写一个"股票筛选器"，筛选涨幅>阈值的股票

stocks = {
        '茅台': {'buy': 1800, 'price': 1850},
        '宁德时代': {'buy': 200, 'price': 195},
        'BYD': {'buy': 250, 'price': 260}
          }
threshold = 0.03
for stock, details in stocks.items():
        rate = (details['price'] - details['buy']) / details['buy']
        remain = (f'{stock} 入选,涨幅{rate:.2%}' if rate > threshold 
                  else f'{stock} 不入选,涨幅{rate:.2%}')
        print(remain)