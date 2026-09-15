stock = {
    'code': '600519',
    'name': '贵州茅台',
    'price': 1888.5,
    'change': 2.35,
    'volume': 3200000,
    'tmp_field': '待删除',    # 临时字段，要删掉
    'unused': '无用数据'      # 无用字段，也要删掉
}
del stock['tmp_field']
print(stock.pop('unused'), stock.get('unused', 0))
print(stock.pop('pe', '无此字段'))
print(stock)