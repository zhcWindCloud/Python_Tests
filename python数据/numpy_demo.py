"""
@Time    : 2021/5/16 11:30
@Author  : ZHC
@FileName: numpy_demo.py
@Software: PyCharm
"""
import numpy as np

# n = input("输入要生成的数组")
n = 2
m = np.arange(7, dtype='f')
print(m, m[2:4])
print("*" * 80)
b = np.arange(24).reshape(2, 3, 4)
print(b)
print("*" * 80)
print("选定第1层楼、第1行、第1列的房间", b[0, 0, 0])
print("*" * 80)
print("选取所有楼层的第1行、第1列的房间", b[:, 0, 0])
print("*" * 80)
print("选取第1层楼、第2排的所有房间：",b[0,1] )
print("*" * 80)
print("选取所有楼层的位于第2列的房间",b[...,1])
print()
print("ravel 我们可以用ravel函数完成展平的操作：",b.ravel())
print()

b.shape = (6,4)
print(b,b.shape)