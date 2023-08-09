# 打好python基础很重要！

# 练习时间：2022/8/6 23:02
class Student(): #Student为类的名称，为类对象。由一个或多个单词组成，每个单词的首字母大写，其余小写
    native_place="汕头" #直接写在类里的变量，称为类属性
    def __init__(self,name,age): #实例化,name, age是局部变量
        self.name = name    #self.name是实例属性，可任意命名为self.xx，进行了赋值操作，将局部变量的name值赋给实体属性
        self.age = age

    #实例方法
    def eat(self):
        print("他正在吃饭")

    @staticmethod
    def method():  #不需要加self
        print("正在使用staticmethod静态方法")
    # 类方法
    @classmethod
    def cm(cls):
        print("正在使用类方法")

 # 创建Student类的实例对象，语法：实例名 = 类名()。有实例，便可以通过指针调用类中的内容
stu1 = Student("张三",20)

print(id(stu1))
print(type(stu1))
print(stu1)
# print(stu1.name)
# print(stu1.age)
print("------------------------------------------")
print(id(Student))
print(type(Student))
print(Student)

# 调用类中的内容
print(stu1.eat())  #对象名.方法名()
print(stu1.name)
print(stu1.age)

print("------------------------------------------")
Student.eat(stu1)  #传入对象。类名.方法名(类的对象) 实际上就是方法定义处的self