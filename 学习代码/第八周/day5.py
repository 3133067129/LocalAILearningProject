# 要求：
# 1. 用 try 打开并读取 stock_data.csv
# 2. except FileNotFoundError: 打印 "File not found, using empty list."
# 3. except PermissionError: 打印 "Permission denied."
# 4. else: 把每一行转成 float，存入 prices
# 5. finally: 打印 "Data loading attempt finished."
# 6. 最后判断 prices 是否为空，为空则不再做后续计算

import csv
filepath = "stock_data.csv"
prices = []

try:
    with open(filepath, mode = 'r', encoding='utf-8') as f:
        rows = list(csv.reader(f))
except FileNotFoundError:
    print("File not found, using empty list.")
except PermissionError:
    print("Permission denied.")
else:
    for row in rows[1:]:
        try:
            prices.append(float(row[4]))
        except ValueError:
            print(f"Warning: invalid price {row}, skipped.")
finally:
    print("Data loading attempt finished.")

if prices:
    print("Data can be calculated!")
else: print("Empty Value")