# 打好python基础很重要！

# 练习时间：2022/8/8 16:13
def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

print(fac(6))

def fib(n):
    if n ==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(6))
