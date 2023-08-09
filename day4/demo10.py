# 打好python基础很重要！

# 练习时间：2022/8/12 10:46

import os
path = os.getcwd()  #返回当前工作目录
# print(path)
lst_files = os.walk(path)   #walk遍历
# print(lst_files)
for dirpath,dirname,filename in lst_files:
    # print(dirpath)
    # print(dirname)
    # print(filename)
    # print("------------------------------")
    for dir in dirname:
        print(os.path.join(dirpath,dir))
    for file in filename:
        print(os.path.join(dirpath,file))
    print("------------------------------")

