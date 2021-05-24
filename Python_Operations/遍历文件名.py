"""
@Time    : 2021/5/15 16:21
@Author  : ZHC
@FileName: 遍历文件名.py
@Software: PyCharm
"""

import os
def file_name(file_dir):
  for root, dirs, files in os.walk(file_dir):
    print(root) #当前目录路径
    print("*" * 90)
    print(dirs) #当前路径下所有子目录
    print("*"*90)
    print(files) #当前路径下所有非目录子文件
    print(len(files))  # 当前路径下所有非目录子文件

if __name__ == '__main__':
    file_dir = r"E:\Img"
    file_name(file_dir)