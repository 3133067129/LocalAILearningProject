"""
在 IDE 中用英文写：

创建 5 天收盘价数组：close_prices = [10.2, 10.5, 10.3, 10.8, 11.0]，用 np.array() 转成数组。

创建 3 个资产、2 种权重的组合矩阵，用 np.zeros((3, 2))。

创建 4 天持仓标记，用 np.ones(4)。

创建 1 到 12 月，用 np.arange(1, 13)。

打印每个数组的 shape 和 dtype。

涉及：np.array、np.zeros、np.ones、np.arange、shape、dtype。写完可把代码发我检查。
"""

import numpy as np

close_prices = [10.2, 10.5, 10.3, 10.8, 11.0]
a = np.array(close_prices)
print(a, a.dtype, a.shape)

b = np.zeros((3,2))
print(b, b.dtype, b.shape)

c = np.ones(4) 
print(c, c.dtype, c.shape)

d = np.arange(1, 13)
print(d, d.dtype, d.shape)