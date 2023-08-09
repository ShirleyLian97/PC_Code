# 打好python基础很重要！

# 练习时间：2022/8/8 11:02
def fun(arg1,arg2):
    print("arg1=",arg1)
    print("arg2=",arg2)
    arg1 = 100
    arg2.append(10)
    print("arg1=", arg1)
    print("arg2=", arg2)

n1 = 10
n2 = [10,20,30]
print("n1",n1)
print("n2",n2)
fun(n1,n2) #位置传参，实参名称与实参名称可以不一致
print("n1",n1) #int不可变对象，在函数体的修改不会影响实参的值 arg1的值修改为100，不会影响n1
print("n2",n2)  #列表可x`变，在函数体的修改会影响实参的值 arg2的值修改 appeng(10)，会影响n2