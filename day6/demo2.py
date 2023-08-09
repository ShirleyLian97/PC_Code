# 打好python基础很重要！

# 练习时间：2022/8/14 11:31
'''1到100之间的偶数和'''
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print(sum)

print("--------------使用while循环-----------")
i=1  #初始化变量
sum_whi=0
while i<101: # 条件判断
    if not i%2:  #循环体
        sum_whi+=i
    i+=1  #改变变量
print(sum)
