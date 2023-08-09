# 打好python基础很重要！

# 练习时间：2022/8/8 19:34
class Car:
    def __init__(self,brand):  #实例属性
        self.brand = brand
    def start(self):
        print("汽车已启动.....")

car = Car("宝马")
car.start()
print(car.brand)

class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age  #不希望在类外被使用
    def show(self):
        print(self.name,self.__age)

stu = Student("张三",24)
stu.show()

print(stu.name)
# print(stu.__age)  #年龄不能在类外被使用