# 打好python基础很重要！

# 练习时间：2022/8/10 23:29
# 导入模块
import math  #导入别人定义好的模块，导入模块里的所有东西
print(id(math))
print(type(math))
print(math)
print(dir(math))
print(math.pi,type(math.pi))
print(math.pow(2,3))
print(type(math.pow(2,3)))
print(math.ceil(9.1))
print(math.floor(9.999))

# 导入模块里的函数/变量/类
from math import pi
print(pi)   #可以直接使用pi
print(pow(2,3))  #使用的是builtins模块
print(math.pow(2,3))  #使用的是math模块

from math import pow
print(pow(2,3)) #因为从math模块导入了pow,所以这里使用的是math模块

import cal
print(cal.add(2,3))
print(cal.div(8,2))

from cal import add
print(add(4,5))
