# 打好python基础很重要！

# 练习时间：2022/8/11 0:10

import package.moduleA
import package.moduleA as ma
print(ma.a)

import package
import cal


# import 后只能接包或模块
# from xx import 后能接包、模块、函数、类、变量等

from package import moduleB as mb
print(mb.b)

from package.moduleA import a
print(a)