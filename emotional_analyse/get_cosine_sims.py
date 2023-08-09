# 打好python基础很重要！

# 练习时间：2022/9/18 22:51
import numpy as np

def cos_sim(a, b):
    vec_a = np.mat(a)
    vec_b = np.mat(b)
    num = float(vec_a*vec_b.T)
    denom = np.linalg.norm(vec_a)*np.linalg.norm(vec_b)
    return num/denom

a = [1,1,1]
b = [2,2,2]
print(cos_sim(a, b))


