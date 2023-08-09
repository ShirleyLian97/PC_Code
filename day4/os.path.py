# 打好python基础很重要！

# 练习时间：2022/8/11 20:50

import os.path
print(os.path.abspath("os.path.py"))  #获得指定文件的绝对路径
print(os.path.exists("demo1.py"),os.path.exists("demo12.py"))
print(os.path.join("D:\\Python","demo1.py")) #join(path,name)，将目录与目录或者文件名拼接起来
print(os.path.split("D:\\python_pycharm\\day4\\os.path.py"))
print(os.path.splitext("os.path.py"))
print(os.path.basename("D:\\python_pycharm\\day4\\os.path.py")) #提取文件名
print(os.path.dirname("D:\\python_pycharm\\day4\\os.path.py"))  #提取目录名，不包括文件名
print(os.path.isdir("D:\\python_pycharm\\day4\\os.path.py"))
print(os.path.isdir("D:\\python_pycharm\\day4"))  #用于判断是否为路径