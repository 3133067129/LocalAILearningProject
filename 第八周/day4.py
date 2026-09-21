# stock_prices 是爬取到的原始字符串列表
stock_prices = ["152.30", "N/A", "148.75", "", "155.20", "abc"]

# 要求：
# 1. 遍历 stock_prices
# 2. 用 try-except 把每个元素转成 float，存入 cleaned_prices
# 3. 转换失败时打印警告信息，并跳过该条数据
# 4. 最后计算 cleaned_prices 的简单收益率（prices[1]-prices[0]）/ prices[0]
#    注意：如果 cleaned_prices 长度不足 2，也要处理

cleaned_prices = []
for stock_price in stock_prices:
    try:
        cleaned_prices.append(float(stock_price))
    except ValueError:
        print("Error")

try:
    print((cleaned_prices[1] - cleaned_prices[0]) / cleaned_prices[0])
except ZeroDivisionError:
    print("zero error")