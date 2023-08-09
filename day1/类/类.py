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
