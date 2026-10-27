"""
变量类型

"""

# 定义变量
a = 695
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "C", "E"]
phones = {"13309091111", "15209109121"}
options = {"count": 0, "total": 0}
goods = ("手机", 5999, 1)

"""
类型注解
    类型注解是python3.5之后出现的一种语法，
    类型注解可以给变量添加类型，
    类型注解可以给函数添加参数和返回值类型
    类型注解可以给类添加属性和成员方法返回值类型
    类型注解可以给模块添加变量和函数返回值类型
    类型注解可以给包添加变量和函数返回值类型
    类型注解可以给包添加模块变量和函数返回值类型
    类型注解可以给包添加包变量和
"""

a2: int = 695
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names1: list[str] = ["A", "C", "E"]
names2: list[str | int] = ["A", "C", "E"]
phones2: set[str] = {"13309091111", "15209109121"}
options2: dict[str, int] = {"count": 0, "total": 0}
goods2: tuple[str, int, int] = ("手机", 5999, 1)

names1.append("X")
# 虽然开发工具提示 类型错误，但是代码可以运行
names1.append(100)
print(names1)

names2.append("X")
names2.append(100)
print(names2)

print("============================================================================")


"""
def 方法名(参数名: 参数类型) -> 返回值类型:
    方法体
"""
def calc_multiply(num: int) -> tuple[int,int]:
    return num * 2, num * 3

print(calc_multiply(2))
