# stock = {'code': '600519', 'name': '贵州茅台', 'price': 1888.5}

# # 遍历所有键值对
# for key, value in stock.items():
#     print(key, "=", value)

# for key, value in stock.items():
#     print(f"{key} = {value}")

# for key, value in stock.items():
#     print(key, value, sep=" = ")


# 创建一个包含两只股票的“大字典”（明天正式学嵌套，今天先感受一下）
portfolio = {
    "茅台": {"code": "600519", "price": 1888.5},
    "宁德": {"code": "300750", "price": 228.5}
}
for name, x in portfolio.items():
        print(f"name = {name}, code = {x['code']}, price = {x['price']}")
# 挑战：用 for 循环把两只股票的 code 和 price 都打印出来
# 提示：你需要两层循环，或者在外层循环里直接用内层字典的键去取值