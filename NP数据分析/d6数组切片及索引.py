# 开发时间：9/10/2022 上午11:48
import numpy as np
arr  = np.arange(10)
print(arr)
print(arr[1])   #np数组中根据索引提取数值  [0 1 2 3 4 5 6 7 8 9]

#一维数组（ np数组中的切片索引
a = slice(2,7,2)  #a为切片设置
print(arr[a])    #ndarray[]为切片内容   [2 4 6]
#or
print(arr[2:7:2])  #[2 4 6]
print(arr[2])   #2
print(arr[2:])   #[2 3 4 5 6 7 8 9]
'''
start:stop:step
stop默认为末尾
step默认为1
'''
'''
多维数组的切片
'''
#多维数组的切片结果为下一维度的元素（二维数组切片出来为一维数组
arr3 = np.arange(15).reshape(5,3)
print(arr3)
print('========切片结果为二维数组中第四行的一维数组===========')
print(arr3[3])
print('========在二维数组中切片结果中再次切片结果为在一维数组中取出单个元素==========')
print('arr3[3][1]的结果为：')
print(arr3[3][1])
print(arr3[3,1])#两种方法相同
print('===========...方法截取，使选择的元组的长度与数组的维度相同==================')
print(arr3[...][1])
print(arr3[1])   #两种方法相同

#
print('\n'
      '\n'
      '\n')
#


print('=============包含省略号...的多维数组切片==========')
arr = np.arange(1,16).reshape(5,3)
print(arr)
print('==============第二列元素=====================')
print(arr[...,1])
print('===============第二行元素===================')
print(arr[1,...])
print('================第二列及后面所有元素===========')
print(arr[...,1:])
print('================第二行及后面所有的元素=========')
print(arr[1:,...])