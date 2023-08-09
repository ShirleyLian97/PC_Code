# 打好python基础很重要！

# 练习时间：2022/8/8 15:46
def func(a,b):
    c = a+b
    print(c)

# print(c)  a,b,c在函数内部定义，为局部变量
# print(a)
# print(b)

name = "莫先生"  #在函数外部定义，为全局变量，可在函数内被调用
print(name)

def func1():
    print(name)

func1()

def func2():
    global age  #定义全局变量
    age = 24
    print(age)
func2()
print(age)