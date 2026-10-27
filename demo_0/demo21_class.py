"""
类和对象
"""
class Car:
    # 类属性
    weels = 4
    tax_rate = 0.4

    def __init__(self, brand, color, name, price):
        # 示例属性
        self.brand = brand
        self.color = color
        self.name = name
        self.price = price
        self.weels = 2

    def running(self):
        print(f"{self.brand},{self.name} 车在跑")

    def total_cost(self, discount, rate):
        return self.price * discount + self.price * rate



car1 = Car("兰博基尼", "黑色", "Lamborghini", 1000000)
car1.running()
# key相同的时候优先使用实例属性
print(car1.weels)
print(car1.tax_rate)

# 获取类属性
print(Car.weels)
print(Car.tax_rate)