stocks = {
        '贵州茅台': {'code': '600519', 'price': 1888.5},
        '宁德时代': {'code': '300750', 'price': 228.5},
        '腾讯控股': {'code': '0700', 'price': 380},
}
fixed_info = ('A股', '消费')

print(stocks.get('宁德时代').get('price'))

stocks['贵州茅台']['price'] = 1900

for x, y in stocks.items():
        print(f"股票名：{x} code： {y.get('code')} price： {y.get('price')}")