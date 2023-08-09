# 打好python基础很重要！

# 练习时间：2022/8/14 12:38

import json
# 准备列表，将其转换为json
data = [{"name":"莫莫","age":11},{"name":"lian","age":21},{"name":"cm","age":22}]
json_str=json.dumps(data,ensure_ascii=False) #表明不使用ascii来转换，直接输出内容
print(type(json_str))  #json为字符串
print(json_str)
# 准备字典，将其转换为json
d={"name":"周杰伦","add":"台北"}
json_str=json.dumps(d,ensure_ascii=False)
print(type(json_str))  #json为字符串
print(json_str)

# 将json字符串转化为pyhon数据类型
s = '[{"name":"莫莫","age":11},{"name":"lian","age":21},{"name":"cm","age":22}]'\
lst=json.loads(s)
print(type(lst))
print(lst)