# 打好python基础很重要！

# 练习时间：2022/8/10 14:42
# python中一切皆对象
a = 10
b = 20
c = a+b  #两个整数类型对象的相加操作,只能是整型加减
d = a.__add__(b)

print(c)
print(d)


class Student():
    def __init__(self,name):
        self.name = name
    def __add__(self, other):  #让两个对象相加的特殊方法
        return self.name+ other.name
    def __len__(self):
        return  len(self.name)

s1 = Student("张三")
s2 = Student("李四")
print(s1 + s2)  #等同于s1.__add__(s2)
print("-------------------------------------------")
lst = [1,2,3,4]
print(len(lst)) #len是内容函数，列表可使用len函数，对象不能使用
print(lst.__len__())
print(len(s1))