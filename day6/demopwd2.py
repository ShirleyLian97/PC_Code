# 打好python基础很重要！

# 练习时间：2022/8/14 11:16

t=0
while t<3:
    pwd=input("请输入密码：")
    if pwd=="8888":
        break  #结束循环，常于if搭配
    else:
        t+=1  #改变变量
        if t<3:
            print("密码错误，请重新输入！")
        else:
            print("输入错误达3次，已被锁定！")

