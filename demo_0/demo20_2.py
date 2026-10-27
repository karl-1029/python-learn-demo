def outer_func():
    class InnerClass:
        def method(self):
            print("我是类方法")

        # 类里面还能嵌套类
        class DeepClass:
            pass

    # 函数里面还能再套函数
    def inner_func():
        print("我是内层函数")

    return InnerClass


# 调用
my_class = outer_func()
obj = my_class()
print(type(obj))
obj.method()