# 打好python基础很重要！

# 练习时间：2022/8/10 11:36
# object类是所有类的父类，因此所有类都拥有object类的属性和方法
class Person():
    pass

stu = Person() #创建对象
print(dir(stu)) #查看对象的属性和方法，从父类object继承而来
print(stu.__str__())  #返回对象的内存地址
print(stu)

class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):  #重写str
        return "我的名字是{},我的年龄是{}".format(self.name,self.age)

stu1 = Student("张三",24)
print(stu1.__str__())
print(type(stu1))