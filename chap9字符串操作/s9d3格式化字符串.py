# 开发时间：9/9/2022 下午3:23
'''
(1)%作为占位符
%s==》字符串
%i或者%d==》整数
%f==》浮点数
'''

name='张三'
age=20
print('我叫%s，今年%d岁' % (name,age))

'''
(2){}作为占位符

'''

print('我叫{0},今年{1}岁'.format(name,age))

'''(3) f-string'''
print(f'我叫{name}，今年{age}岁')



'''
表示精度和宽度
'''
print('%10d' % 99)  #10表示的是宽度
print('%.3f' % 3.1415926)  #.3表示为保留3个小数
#同时表示宽度和精度
print('%10.3f' % 3.1415926)  #一共宽度为10，保留小数点后3位

'''使用{}进行表示宽度和精度'''
print('{0:.3}'.format(3.1415926))  #{0:.3}表示为一共3位数字
print('{:.3f}'.format(3.1415926))
print('{:10.3f}'.format(3.1415926))  #同时设置精度和宽度，一共是10位，3位是小数