import csv
filepath = 'stock_data.csv'
output_path = 'summary.csv'
close_prices = []

try:
    with open(filepath, newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f))
except FileNotFoundError:
    print(f"{filepath} not found")
else:
    for row in rows[1:]:
        try:
            close_prices.append(float(row[4]))
        except (ValueError, IndexError):
            print(f"invalid row: {row}, skipped.")

    if close_prices:
        count = len(close_prices)
        mean_close = sum(close_prices) / count
        max_close = max(close_prices)
        min_close = min(close_prices)
        print(f"总共{count}个值,平均值{mean_close},最大值{max_close},最小值{min_close}")
    else:
        print("close_prices is empty value")
finally:
    print("Processing finished")

with open(output_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["metric", "value"])
    writer.writerow(["mean_close", mean_close])
    writer.writerow(["max_close", max_close])
    writer.writerow(["min_close", min_close])
    writer.writerow(["count", count])