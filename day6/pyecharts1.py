# 打好python基础很重要！

# 练习时间：2022/8/14 22:27
# 导包，导入Line功能
from pyecharts.charts import Line

# 得到折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["中国","英国","美国"])
# 添加y轴数据
line.add_yaxis("GDP",[30,20,10])
# 生成图表
line.render()  #render方法