# 打好python基础很重要！

# 练习时间：2022/8/7 17:13
class Student:
    def __init__(self,name,age): #定义初始化方法
        self.name = name  #将局部变量值赋给实例变量
        self.age = age
    def eat(self):  #定义方法
        print(self.name+"在吃饭")

#创建实例对象
stu1 = Student("张三",20)
stu2 = Student("李四",30)
print(id(stu1))
print(id(stu2))
print("----------------为stu2动态绑定性别属性-----------")
stu2.gender = "女"
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)

def show():
    print("定义在类之外的，称为函数")

stu1.show = show  #将函数绑定到对象，使其成为对象的方法
stu1.show()  #stu1调用show方法
#stu2.show() #stu2没有绑定show方法

