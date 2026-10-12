"""
鸭子类型
"""


class Duck:

    def __init__(self, name):
        self.name = name

    def swimming(self):
        print(f"{self.name} is swimming")


class Pig:

    def __init__(self, name):
        self.name = name

    def swimming(self):
        print(f"{self.name} is swimming")


class Dog:

    def __init__(self, name):
        self.name = name

    def swimming(self):
        print(f"{self.name} is swimming")


def global_swimming(duck):
    duck.swimming()



"""
鸭子类型: 
    不关心类型(类名是否一样)，只关心方法(方法名字一样)
"""
if __name__ == '__main__':
    duck = Duck("小鸭")
    pig = Pig("小猪")
    dog = Dog("小狗")

    global_swimming(duck)
    global_swimming(pig)
    global_swimming(dog)

    print("可以看到虽然global_swimming() 接收的参数是Duck，但是传入的参数是Pig，Dog，但是程序会执行Duck的swimming()方法")
    print("表现了多态行为 但是这几个类没有继承关系")
