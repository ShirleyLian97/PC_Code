# 打好python基础很重要！

# 练习时间：2022/8/10 16:06
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk

# 变量的赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(cpu2)

# 浅拷贝：对象包含的子对象内容不拷贝，因此，源对象与拷贝对象都会引用同一个子对象
# 类有浅拷贝
disk = Disk() #创建一个硬盘类的对象

computer = Computer(cpu1,disk)  #创建一个计算机类的对象

# 浅拷贝
import copy
computer2 = copy.copy(computer)  #拷贝computer的内存到computer2里存着
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
print("--------------------------------------------")

# 深拷贝
computer3 = copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)