import csv

"""默认以字符串方式读取csv文件"""
# with open('data.csv', mode='r', encoding='utf-8') as f:
#     csv_reader = csv.reader(f)

#     for row in csv_reader:
#         print(row)

"""csv写入"""
# data = [
#     ['Name', 'Age', 'City'],
#     ['Alice', '30', 'New York'],
#     ['Bob', '25', 'Los Angeles']
# ]

# with open('output.csv', mode='w', encoding='utf-8', newline='') as file:
#     csv_writer = csv.writer(file)

#     for row in data:
#         csv_writer.writerow(row)

"""以字典方式读取csv文件"""
# with open('stock_data.csv', mode='r', encoding='utf-8') as file:
#     csv_dict_reader = csv.DictReader(file)

#     for row in csv_dict_reader:
#         print(row)

"""以字典方式写入csv文件"""
data = [
    {'Name': 'Alice', 'Age': '30', 'City': 'New York'},
    {'Name': 'Bob', 'Age': '25', 'High': '173', 'City': 'Los Angeles'}
]
with open('output.csv', mode='w') as file:
    fieldnames = ['Name', 'Age', 'City', 'High']
    csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_dict_writer.writeheader()

    for row in data:
        csv_dict_writer.writerow(row)


