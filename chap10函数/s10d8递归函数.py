# 开发时间：13/9/2022 下午2:06
'''
递归函数：在一个函数的函数体内调用了该函数本身，这个函数就称为递归函数
其中包含递归函数和递归终止条件
'''

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(10))
