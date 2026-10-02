"""
函数
"""


# 方法嵌套调用


def method_a():
    print("========method_a=======")
    method_b()


def method_b():
    print("========method_b=======")
    method_c()


def method_c():
    print("========method_c=======")


def method_call():
    print("========method_call=======")
    method_a()


method_call()


# 定义一个求三角形面积的函数
def triangle_area(base, height):
    """
    计算三角形面积
    :param base: 底
    :param height: 高
    :return:
    """
    return round(base * height / 2, 2)


print(f"面积: {triangle_area(10, 5):.2f}")


# 定义一个统计字符串中元音字母的个数
def count_vowel(str):
    """
    统计字符串中元音字母的个数
    :param str:
    :return:
    """
    result = 0
    for item in str:
        if item in "aeiou":
            result = result + 1
    return result


print(f"统计元音字母的个数: {count_vowel("hello-python")}")


# 定义一个求最大值 最小值 平均值的方法 并且返回
def max_min_avg(nums):
    """
    求最大值 最小值 平均值
    :param nums:
    :return:
    """
    max_num = max(nums)
    min_num = min(nums)
    avg = round(sum(nums) / len(nums), 2)
    return max_num, min_num, avg


max, min, avg = max_min_avg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"最大值: {max}")
print(f"最小值: {min}")
print(f"平均值: {avg}")
