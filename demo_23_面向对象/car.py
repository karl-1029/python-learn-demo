"""
创建一个汽车类，属性有颜色，品牌，名称，拥有者，方法有启动，行驶，停止，获取拥有者。

继承
class 类名(父类名):
    pass

会将父类的非私有的属性/方法继承过来。

多态

"""
from ctypes import GetLastError


class Car:

    def __init__(self, color, brand, name, owner):
        self.color = color
        self.brand = brand
        self.name = name
        self.__owner = owner  # 私有属性

    def start(self):
        print(f"{self.brand} {self.name} 正在启动...")

    def running(self):
        print(f"{self.brand} {self.name} 正在行驶...")

    def stop(self):
        print(f"{self.brand} {self.name} 正在停止...")

    def charge(self):
        print(f"{self.brand} {self.name} charge 正在补充燃料...")

    def get_owner(self):
        return self.__owner


class FuelCar(Car):
    def charge(self):
        # 调用父类方法2种格式 推荐super().方法名()
        print("调用父类方法 charge ...")
        super().charge()
        Car.charge(self)
        print(f"{self.brand} {self.name} charge 正在加油...")


class ElectricCar(Car):
    def charge(self):
        print(f"{self.brand} {self.name} charge 正在充电...")


# 创建一个方法，参数为Car对象，方法内部调用Car对象的charge方法
def handler_charge(car: Car):
    car.charge()


if __name__ == '__main__':
    car_father = Car("蓝色", "保时捷", "911", "小王")
    print(car_father.color)
    print(car_father.brand)
    print(car_father.name)
    # print(car.__owner)          #   错误    不可以直接访问私有属性
    print(car_father._Car__owner)  # _类型_属性名称 可以访问私有属性

    car_father.start()
    car_father.running()
    car_father.stop()
    print(car_father.get_owner())
    car_father.charge()

    print("===========================测试继承/重写=================================")
    fuelCar_son = FuelCar("蓝色1", "保时捷1", "911-1", "小李")
    print(fuelCar_son.color)
    print(fuelCar_son.brand)
    print(fuelCar_son.name)
    print(fuelCar_son.get_owner())
    fuelCar_son.start()
    fuelCar_son.running()
    fuelCar_son.stop()
    fuelCar_son.charge()

    electricCar_son = ElectricCar("蓝色2", "保时捷2", "911-2", "小王")
    print(electricCar_son.color)
    electricCar_son.charge()


    print("===========================测试多态=================================")
    handler_charge(fuelCar_son)
    handler_charge(electricCar_son)
