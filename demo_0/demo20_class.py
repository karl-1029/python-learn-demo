"""
类和对象
"""


# version 1
class Car:
    pass


car = Car()
car.name = "兰博基尼"
car.price = "1000w"
print(car)
print(car.name)
print(car.__dict__)
print(type(car))

print("============================================================================")


# version 2 __init__方法
class Car:
    def __init__(self, brand, color, name, price):
        self.brand = brand
        self.color = color
        self.name = name
        self.price = price
        print("__init__方法被调用 对象初始化")


c1 = Car("兰博基尼", "黑色", "Lamborghini", "1000w")
print(c1.__dict__)

c2 = Car("兰博基尼", "红色", "Lamborghini", "900w")
print(c2.__dict__)

# version 3 属性+方法+魔法方法
print("==================================version 3==========================================")


class Car:
    def __init__(self, brand, color, name, price):
        self.brand = brand
        self.color = color
        self.name = name
        self.price = price

    def running(self):
        print(f"{self.brand},{self.name} 车在跑")

    def total_cost(self, discount, rate):
        return self.price * discount + self.price * rate

    # 重写魔法方法 __xxx__
    def __str__(self):
        return f"魔法方法__str__ : {self.brand}, {self.name}"

    def __eq__(self, other):
        return self.brand == other.brand and self.color == other.color and self.name == other.name and self.price & other.price


car1 = Car("兰博基尼", "黑色", "Lamborghini", 1000000)
print(car1)
car1.running()
print(f"提车价格: {car1.total_cost(0.8, 0.1)}")

# 比较2个对象是否相等
car2 = Car("兰博基尼", "黑色", "Lamborghini", 1000000)
car3 = Car("兰博基尼", "黑色", "Lamborghini", 1000001)
print(car1 == car2)
print(car1 == car3)
