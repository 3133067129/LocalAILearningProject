import numpy as np

close_prices = np.array([10.2, 10.5, 10.3, 10.8, 11.0])
returns = np.array([[0.01, -0.02], [0.03, 0.00], [0.02, -0.01]])
arrays = {"close_prices": close_prices, "returns": returns}
for name, array in arrays.items():
    print(f".shape of {name} is {array.shape}\n" 
          f".ndim of {name} is {array.ndim}\n"  
          f".size of {name} is {array.size}\n"
          f".dtype of {name} is {array.dtype}\n")
"""
shape 维度
ndim 秩
size 元素的总个数
dtype 数据类型
"""