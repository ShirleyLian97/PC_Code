# 打好python基础很重要！

# 练习时间：2022/8/11 17:50

import os    #系统自带的模块
# os.system("notepad.exe")
# os.system("calc.exe")

# 直接调用可执行文件
# os.startfile("D:\\Program Files\\网易云音乐\\CloudMusic\\cloudmusic.exe")

os.getcwd()
lst = os.listdir("../day4")  #返回指定路径下的文件和目录信息
print(lst)

# os.mkdir("mkdir")
# os.makedirs("A/B/C")
# os.rmdir("mkdir")  #删除指定文件
# os.removedirs("A/B/C")
os.chdir("D:\\python_pycharm\\day4")
print(os.getcwd())