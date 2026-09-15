num1, num2, i, n= 1, 2, 2, 10
print(f"NO.1: {num1} \nNO.2: {num2}")
while i < n:
        num3, num2, i= num2, num1 + num2, i + 1
        print(f"NO.{i}: {num2}")
        num1 = num3