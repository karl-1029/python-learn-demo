"""
函数参数传递
    不定长参数
        位置参数    *args
        关键参数    **kwargs

"""


def calc(*args, **kwargs):
    print(f"不定长参数位置参数:{type(args)}")
    print(f"不定长参数关键字参数:{type(kwargs)}")
    max_num = max(args)
    min_num = min(args)
    avg_num = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_num = round(avg_num, kwargs.get("round"))

    if kwargs.get("printFlag"):
        print(f"kywords: {kwargs}")

    return max_num, min_num, avg_num


# 测试不定长参数 位置参数
print(calc(1, 2, 5, 7, 8))
print(calc(6, 50, 10, 20, 30, 40, 50))

print("============================================================================")

# 测试不定长参数 关键字参数
print(calc(1, 2, 3, 5, 7, 9, 11, round=3, printFlag=True, name="tom"))
