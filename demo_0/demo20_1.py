class Person:
    # 类属性（属于类，所有实例共享）
    species = "人类"

    def __init__(self, name, age):
        # 实例属性（属于每个对象）
        self.name = name
        self.age = age

    # ✅ 实例方法：第一个参数 self，操作实例自己的数据
    def say_hello(self):
        print(f"你好，我是{self.name}，今年{self.age}岁")

    # ✅ 类方法：@classmethod，第一个参数 cls，操作类属性
    @classmethod
    def show_species(cls):
        print(f"物种：{cls.species}")
        # 类方法也可以用来构造对象（工厂方法）
        return cls("默认名字", 18)

    # ✅ 静态方法：@staticmethod，没有 self / cls，和类、实例弱关联，只是挂在类下面的工具函数
    @staticmethod
    def is_adult(age):
        return age >= 18


# ========== 测试调用 ==========



if __name__ == "__main__":
    # 实例
    p1 = Person("Carl", 33)

    # 调用实例方法：必须用实例调用
    p1.say_hello()

    # 调用类方法：实例、类名都可以调用
    Person.show_species()
    p1.show_species()

    # 调用静态方法：实例、类名都可以调用
    print(Person.is_adult(20))
    print(p1.is_adult(15))

    # 类方法工厂新建对象
    p2 = Person.show_species()
    p2.say_hello()
