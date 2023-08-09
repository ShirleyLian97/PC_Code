# 打好python基础很重要！

# 练习时间：2022/8/8 11:36

def func(num):
    odd = []
    even = []
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

print(func([10,29,34,23,44,53,55]))

'''
函数的返回值
（1）如果函数没有返回值，即函数执行完毕之后，不需要给调用处提供数据，return可省略
（2）函数的返回值，如果返回值为1个，则直接返回类型
（3）函数的返回值，如果返回值为多个，返回元组


'''

def func1():
    print("hello world")

func1()

def func2():
    return "hello world"

res = func2()
print(res)

def func3():
    return"hello","world"

print(func3())

print("hello",end="\t")  默认断行
print("world")