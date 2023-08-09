# 打好python基础很重要！

# 练习时间：2022/8/11 12:10

png = open("framework.png","rb")  #png不是文本，而是图片，图片、音频等是二进制形式，需用b
target_png = open("target_png.png","wb")
target_png.write(png.read())
png.close()
target_png.close()