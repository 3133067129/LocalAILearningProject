stock = {
        'code': '300750', 'price': 228.5, 'change': '1.25', 'volume': '150000', 'pe': 22.3
}
print(stock['price'], stock['volume'], sep='\n')
stock['price'] = 230.0
print(stock['price'])
stock['high'] = 232.0
print(stock.get('dividend', 0))