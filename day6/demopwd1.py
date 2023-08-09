# 打好python基础很重要！

# 练习时间：2022/8/14 11:07
t=0
for i in range(3):
    pwd=input("请输入密码：")
    if pwd=="8888":
        print("密码正确")
        break  #跳出循环，常于if搭配
    else:
        t+=1
        if t<3:
            print("密码不正确，请重新输入")
        else:
            print("输入错误达3次，已被锁定！")


print("===========================================")





