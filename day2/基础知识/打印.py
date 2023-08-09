# 打好python基础很重要！

# 练习时间：2022/8/8 10:32
import os

fp = open("D:/test.text","a+")  #a+如果文件不存在就创建，文件存在就在后面追加
print("hello world",file=fp)
fp.close()

os.remove("D:/test.text")