# 打好python基础很重要！

# 练习时间：2022/8/6 23:02
class Student(): #Student为类的名称，由一个或多个单词组成，每个单词的首字母大写，其余小学
    native_place="汕头" #直接写在类里的变量，称为类属性
    def __init__(self,name,age): #实例化,name, age是局部变量
        self.name = name    #self.name是实体属性，可任意命名为self.xx，进行了赋值操作，将局部变量的name值赋给实体属性
        self.age = age

    #实例方法，在类之外定义的函数为函数，类之内定义的函数称为方法
    def eat(self):
        print("他正在吃饭")

    @staticmethod
    def method():  #不需要加self
        print("正在使用staticmethod")

    @classmethod
    def cm(cls):
        print("正在使用类方法")

# 类属性的使用方法
print(Student.native_place)
stu1 = Student("张三",20) #创建对象1
stu2 = Student("李四",30)   #创建对象2
print(stu1.native_place)
print(stu2.native_place)
Student.native_place = "阳江"   #修改类属性后，类中的实例对象通过指针访问到的值也会随之变化
print(stu1.native_place)
print(stu2.native_place)


print("-----------类方法的调用-------------------------------")
Student.cm()  #使用类名直接访问
Student.method()