# 打好python基础很重要！

# 练习时间：2022/8/12 18:03

try:
    a = int(input("请输入第一个整数"))
    b = int(input("请输入第二个整数"))
    result = a/b

except BaseException as e:
    print("出错了",e)

else:
    print("结果为:",result)
finally:
    print("谢谢您的使用！")