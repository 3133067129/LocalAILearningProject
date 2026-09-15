stocks = {
        '贵州茅台': {'code': '600519', 'price': 1888.5},
        '宁德时代': {'code': '300750', 'price': 228.5},
}
fixed_info = ('A股', '消费')

stocks['五粮液'] = {'code': '000858', 'price': 150.0}

stocks['宁德时代']['price'] = 230.0

print(stocks.get('贵州茅台').get('pe', '暂无'))

if stocks.get('腾讯控股'):
        stocks['腾讯控股'].pop('volume')