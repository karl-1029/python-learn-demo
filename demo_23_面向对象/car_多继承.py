"""
多继承
class 类名(父类名1, 父类名2):
    pass
"""


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


class HuaWeiAiCar():
    def __init__(self, version="1.0"):
        self.version = version

    def running(self):
        print("华为智能车正在行驶...")


"""
多继承了

多继承的时候顺序:
method solution order :
    优先使用第一个继承的同名属性/方法
"""


class WenJieCar(Car, HuaWeiAiCar):
    """
    多继承
    class 类名(父类名1, 父类名2):
        pass
    """

    def __init__(self, color, brand, name, owner, version="1.0"):
        Car.__init__(self, color, brand, name, owner)
        HuaWeiAiCar.__init__(self, version)

    def running(self):
        Car.running(self)
        HuaWeiAiCar.running(self)
        print("WenJieCar 正在行驶...")


if __name__ == '__main__':
    wenjieCar = WenJieCar("蓝色", "保时捷", "911", "小王", "V5.0")
    print(wenjieCar.name)
    print(WenJieCar.mro())
    print(WenJieCar.__mro__)

    print(wenjieCar.__dict__)
    wenjieCar.running()
