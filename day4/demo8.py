# 打好python基础很重要！

# 练习时间：2022/8/11 17:44

with open("framework.png","rb") as src_file:
    with open("copy_frame.png","wb") as target_file:
        target_file.write(src_file.read())