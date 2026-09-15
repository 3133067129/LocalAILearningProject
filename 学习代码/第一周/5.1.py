# 示例：用字典存储股票信息
stocks = {
    'AAPL': {'name': '苹果', 'price': 175.50, 'change': 0.5},
    'GOOGL': {'name': '谷歌', 'price': 141.80, 'change': -0.3},
    'TSLA': {'name': '特斯拉', 'price': 245.30, 'change': 2.1}
}

x = int(input("你要添加几个股票："))
for i in range(x):
    code = input("股票代码：")
    name = input("股票名称：")
    price = float(input("收盘股价："))
    change = float(input("波动率："))
    info = {'name': name, 'price': price, 'change': change}
    stocks[code] = info
print(stocks)


# 练习操作：
# 1. 添加一只新股票
# 2. 修改某只股票的价格
# 3. 删除一只股票
# 4. 遍历字典打印所有股票信息
# 5. 查找并打印价格最高的股票