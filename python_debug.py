# 打好python基础很重要！

# 练习时间：2022/11/28 10:20

def sum_demo(x,y):
    for _ in range(10):
        x+=1
        y+=1
        result=x+y
    return result

if __name__=='__main__':
    result=sum_demo(1,1)
    print(result)