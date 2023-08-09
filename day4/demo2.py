
# 打好python基础很重要！

# 练习时间：2022/8/11 11:27
# 不同编码格式影响着磁盘占用空间
# python解释器使用的是Unicode(内存)
# .py文件在磁盘上使用UTF-8存储（外存）
# gbk,英文1个字节，汉字2个字节
# UTF-8，英文1个字节，汉字3个字节

file = open("bb.txt","w")
file.write("helloworld")
file.close()