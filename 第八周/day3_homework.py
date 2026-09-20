import csv

with open('stock_data.csv', mode='r', encoding='utf-8') as f:
    stock = csv.reader(f)
    i = 0
    next(stock)
    for row in stock:
        if i < 5:
            print(f"Date: {row[0]}, Open: {row[1]}, High: {row[2]},"
                f"Close: {row[3]}, Volume: {row[4]}")
            i += 1
        else:
            break
