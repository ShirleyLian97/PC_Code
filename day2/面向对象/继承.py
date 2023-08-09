# 打好python基础很重要！

# 练习时间：2022/8/8 19:42

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

class Teacher(Person):
    def __init__(self,name,age,year):
        super(Teacher, self).__init__(name,age)
        self.year = year

stu = Student("张三",24,90)
tea = Teacher("李四",40,8)
stu.info()
tea.info()

