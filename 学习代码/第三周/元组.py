'''
创建一个元组 stock，保存股票信息：代码 "000001"、名称 "平安银行"、现价 10.52

用索引取出股票名称并打印

尝试修改现价为 11.00，观察发生了什么

用 len(stock) 查看元组有几个元素

把元组解包赋值给三个变量 code, name, price，然后打印它们
'''

# stock = ('000001', '平安银行', '10.52')
# name = stock[1]
# print("股票名称：", name, "\n元素数量：" ,len(stock))
# for i in range(len(stock)):
#         if i == 0:
#                 code = stock[i]
#                 print('股票代码：', code)
#         if i == 1:
#                 name = stock[i]
#                 print('股票名称：', name)
#         else:
#                 price = stock[i]
#                 print('现价：', price)

'''
进阶挑战：
创建一个包含多只股票的元组列表（即列表的每个元素都是一个元组），然后用 for 循环遍历打印每只股票的名称和价格。
'''
stock = [('000001', '平安银行', '10.52'), ('000002', '工商银行', '10.60'), ('000003', '建设银行', '10.70')]
for i in stock:
        code, name, price = i
        print(f'股票代码：{code}\n股票名称：{name}\n现价：{price}')
