# 开发时间：16/9/2022 下午2:11
'''
面向对象的三大特征
1.封装：可以提高程序的安全性（将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，在类对象化的外部调用方法
这样，无需关心方法内部的具体实现细节，从而隔离了复杂度。

2.继承：提高代码的复用性
3.多态：提高程序的可扩展性和可维护性
'''

class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动')     #封装

car=Car('奔驰300')
car.start()
print(car.brand)
