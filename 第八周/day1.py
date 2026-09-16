def high_price_date(files_local, fields = []):
    with open(files_local, "r", encoding="utf-8") as f:
        for line in f.readlines():
            clear_line = line.strip()
            fields.append(clear_line.split(","))

        for field in fields:
            date_str = field[0]
            price = float(field[1])
            if price > 183:
                print(date_str, price)            

file = r"D:\projects\LocalAILearningProject\第八周\stock_prices.txt"
high_price_date(file)
