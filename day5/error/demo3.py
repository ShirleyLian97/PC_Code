# 打好python基础很重要！

# 练习时间：2022/8/12 18:03

try:
    a = int(input("请输入第一个整数"))
    b = int(input("请输入第二个整数"))
    result = a/b
    print("结果为：",result)
except ZeroDivisionError:
    print("对不起，除数不为0")
except ValueError:
    print("只能输入数字串")

print("程序结束")