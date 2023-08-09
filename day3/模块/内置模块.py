# 打好python基础很重要！

# 练习时间：2022/8/11 0:54

#sys:与python解释器及其环境操作相关的标准库

import sys
print(sys.getsizeof(24))    #模块名.xx调用模块里的方法，此处为获取对象的内存大小
print(sys.getsizeof(48))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

import time
print(dir(time))
print(time.time())
print(time.localtime(time.time()))

import urllib.request         #urlib是一个包，因为有init模块,request模块是urllib的一个模块
print(urllib.request.urlopen("http://www.baidu.com").read())   #urlopen是request模块的一个方法，可用于爬虫

import schedule

def job():
    print("哈哈——————")

# schedule.every(2).seconds.do(job)
# schedule.every(2).to(7).seconds.do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)