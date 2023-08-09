# 打好python基础很重要！

# 练习时间：2022/8/11 16:48

# with语句可以自动管理上下文资源，无论什么原因跳出with块，都能保证文件正确的关闭，以此来达到释放资源的目的

with open("aa.txt","r") as file:
    print(file.read())  #自动释放资源，无需手动关闭文件

class MycontentMgr(object):
    def __enter__(self):
        print("enter方法被调用执行了")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit方法被调用执行了")

    def show(self):
        print("show方法被调用执行了")

with MycontentMgr() as file:  #相当于file = MyContentMgr()
    file.show()
