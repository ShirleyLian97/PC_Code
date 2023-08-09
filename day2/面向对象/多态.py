# 打好python基础很重要！

# 练习时间：2022/8/10 11:59
class Animal(object):
    def eat(self):
        print("动物要吃东西")

class Dog(Animal):
    def eat(self):
        print("狗要吃骨头")

class Cat(Animal):
    def eat(self):
        print("猫要吃鱼")

class Person:
    def eat(self):
        print("人要吃五谷杂粮")
# 定义一个函数
def func(obj):
    obj.eat()

func(Animal())
func(Dog())
func(Cat())
func(Person())

# 静态语言实现多态的必要条件：
# 继承、方法重写、父类引用指向子类对象