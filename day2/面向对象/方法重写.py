# 打好python基础很重要！

# 练习时间：2022/8/10 11:24
# 如果子类对继承父类的某个属性或方法不满意，可以在子类中对其方法体进行重新编写。重写后，可以通过super().xx调用
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)  #super函数调用父类的方法,将name,age传入
        self.score = score
    def info(self):
        super().info()
        print("分数:{}".format(self.score))

class Teacher(Person):
    def __init__(self,name,age,year):
        super(Teacher, self).__init__(name,age)
        self.year = year
    def info(self):
        super().info()
        print("教龄:{}".format(self.year))

stu = Student("张三",24,90)
tea = Teacher("李四",40,8)
stu.info()
tea.info()