prices = {
    "茅台": [1800, 1820, 1810, 1830],
    "宁德时代": [200, 195, 198, 205],
    "BYD": [250, 255, 252, 260],
}
# 法一
# for a, b in prices.items():
#         for i in range(len(b)):
#                 print(f"{a} 第{i+1}天： {b[i]}")

# 法二：使用enumerate()
for stock, price_list in prices.items():
        for day, price in enumerate(price_list, start = 1):
                print(f"{stock} 第{day}天： {price}")
        avg = sum(price_list) / len(price_list)
        print(f"{stock} 均价: {avg:.2f}")