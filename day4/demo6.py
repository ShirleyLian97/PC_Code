# 打好python基础很重要！

# 练习时间：2022/8/11 16:21

file = open("aa.txt","r")
file.seek(2)   #跳过一个中文字符
print(file.read())
print(file.tell())
file.close() #释放文件对象相关资源