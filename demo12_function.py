"""
函数
"""


def print_line():
    print("=========定义函数=======")


print_line()

print("================================================================")


def circle_area(r):
    """
    计算圆的面积------这个是函数的说明文档
    :param r: 半径
    :return: 面积
    """
    return 3.14 * r * r


help(circle_area)
circle_result = circle_area(10)
print(circle_result)

print("================================================================")


def rectangle_area(l, w):
    """
    计算矩形的面积
    :param l: 边长
    :param w: 宽度
    :return:
    """
    return l * w


rectangle_result = rectangle_area(10, 5)
print(rectangle_result)

print("==========================函数返回值有多个======================================")


# 函数返回值有多个
def calc_multiply(num):
    """
    计算乘数
    :param num:
    :return:
    """
    return num * 2, num * 3


# 调用函数结果被组包后，结果被返回给元组变量
calc_result = calc_multiply(20)
print(calc_result)
print(type(calc_result))

# 调用函数结果被解包后，结果被返回给每个变量
multiply_2, multiply_3 = calc_multiply(20)
print(multiply_2)
print(multiply_3)
