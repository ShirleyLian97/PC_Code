# 打好python基础很重要！

# 练习时间：2022/8/14 11:23
'''要求输入1到50之间5的所有倍数'''
lst=[]
for i in range(1,51):
    if i%5==0:
        lst.append(i)

print(lst)

print("----------使用continue-----------")

for i in range(1,51):
    if i%5!=0:
        continue
    else:
        print(i)

