# 打好python基础很重要！

# 练习时间：2022/8/10 15:14
class Person(object):
    def __new__(cls, *args, **kwargs):  #用于创建对象
        print("__new__被调用执行了，cls的id为{}".format(id(cls)))
        obj = super().__new__(cls)
        print("创建的对象的id为:{}".format(id(obj)))
        return obj
    def __init__(self,name,age):  #初始化实例对象的属性
        print("__init__被调用了,self的id为:{}".format(id(self)))
        self.name = name
        self.age = age

print("object类对象的id为:{}".format(id(object)))
print("Person类对象的id为:{}".format(id(Person)))
p1 = Person("张三",24)
print("p1这个Person类的对象的id为:{}".format(id(p1)))
