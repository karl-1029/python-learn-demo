"""
08070 《Python语言程序设计基础教程》代码练习

"""


# 从键盘输入一个正整数n，判断n是否是素数。
def test_1():
    n = int(input("请输入一个正整数:"))
    for i in range(2, n):
        if i % n == 0:
            print(n, "不是素数")
            break
    else:
        print(n, "是素数")


'''
题目：找出所有 4 位的四叶玫瑰数（1000~9999），满足：每一位数字的 4 次方相加 = 数字本身。
最后把结果用逗号连接输出。
1563
'''
def test_2_1():
    result = []
    for i in range(1000, 10000):
        q = i // 1000
        b = i // 100 % 10
        s = i // 10 % 10
        g = i % 10

        sum = q ** 4 + b ** 4 + s ** 4 + g ** 4
        if sum == i:
            result.append(i)
    print(result)

def test_2_2():
    result = []
    for i in range(1000, 10000):
        sum = 0
        for ch in str(i):
            sum += int(ch)**4
        if sum == i:
            result.append(i)
    print(result)

def test_2_3():
    result = [i for i in range(1000, 10000) if sum(int(ch) ** 4 for ch in str(i)) == i]
    print(result)



"""
题目：定义函数 `find_positions(main_str, sub_str)`，
找出子串 `sub_str` 在主串 `main_str` 里面**全部出现的起始索引**（允许重叠查找）。
 测试数据：`main_str='abcabcdeabcdefg'`，`sub_str='abc'`，预期输出 `[0,3,8]`
"""

def test3_find_positions():
    main_str="abcabcdeabcdefg"
    sub_str = "abc"
    start = 0
    result = []
    while True:
        index = main_str.find(sub_str,start)
        if index == -1:
            break
        result.append(index)
        start = index + len(sub_str)
    print(result)


"""
## 第 3 题：文件统计小写字母（函数实现）

题目：写一个函数 `count_lowercase(line)`，统计一行字符串里面小写字母数量。 主程序：打开同目录下 `data.txt`，逐行读取，行号从 1 开始，调用函数，打印：`第 X 行小写字母个数: N`
"""

if __name__ == "__main__":
    # test_1()
    test_2_1()
    test_2_2()
    test_2_3()
    test3_find_positions()
