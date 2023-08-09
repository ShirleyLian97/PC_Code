# 打好python基础很重要！

# 练习时间：2022/8/10 14:28
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name #实例属性
        self.age = age
class D(A):
    pass

# 创建C类对象
c = C("Jack",20) #c是C类的一个实例对象
print(c.__dict__)  #dict获得类对象或实例对象所绑定的所有属性和方法的字典，这里是获取c实例对象的属性
print(C.__dict__) #获取类对象的属性和方法
print("--------------------------------------")
print(c.__class__)  #输出对象所属的类
print(C.__bases__)  #输出父类的元素
print(C.__base__)  #输出第一个父类
print(C.__mro__)  #查看类的层次结构
print(A.__subclasses__()) #输出子类的列表


