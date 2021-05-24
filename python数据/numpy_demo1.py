"""
@Time    : 2021/5/16 11:30
@Author  : ZHC
@FileName: numpy_demo.py
@Software: PyCharm
"""

import numpy as np

a = np.arange(9).reshape(3, 3)
print(a)
print()
b = 2 * a
print(b)
print("水平组合 ",np.hstack((a,b)))
print()
print("用concatenate函数来实现同样",np.concatenate((a,b),axis=1))