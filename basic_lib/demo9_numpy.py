# -*- coding: utf-8 -*-
"""
numpy模块学习Demo
用途：高性能数值计算库，核心是ndarray多维数组；用于数据分析、矩阵运算、数值建模；面试重点：数组创建、变形、切片、聚合、广播、矩阵运算。

【常用方法清单】
1. np.array()：从列表创建ndarray数组
2. np.zeros()：创建全0数组
3. np.ones()：创建全1数组
4. np.arange()：生成等差整数序列
5. np.linspace()：生成指定数量的等间距数值
6. arr.reshape()：改变数组形状，不修改数据
7. arr.T / arr.transpose()：数组转置
8. arr.sum()：数组求和
9. arr.mean()：求平均值
10. arr.max() / arr.min()：求最大值、最小值
11. np.dot()：矩阵点乘（矩阵乘法）
12. 数组切片arr[行,列]：多维数组取值
13. arr.astype()：修改数组数据类型
14. np.concatenate()：拼接多个数组
15. np.random.rand()：生成0~1随机数组
"""
import numpy as np


# 1. 创建数组：np.array
def demo_array_create_1d():
    print("\n================demo_array_create_1d================")
    lst = [1, 2, 3, 4]
    arr = np.array(lst)
    print("np.array创建数组: \n", arr)
    print("数组类型：", type(arr))
    print("数组维度：", arr.ndim)
    print("数组形状(几行几列)：", arr.shape)


def demo_array_create_2d():
    print("\n==============demo_array_create_2d==================")
    lst = [[1, 2, 3], [4, 5, 6]]
    arr = np.array(lst)
    print("创建二维数组: \n", arr)
    print("数组维度:", arr.ndim)
    print("数组形状(几行几列):", arr.shape)


def demo_array_calc():
    print("\n==============demo_array_calc==================")
    lst1 = [1, 2, 3, 4]
    lst2 = [6, 7, 8, 9]
    arr1 = np.array(lst1)
    arr2 = np.array(lst2)

    # 矩阵运算
    print(arr1 + 10)  # 矩阵加10  [11 12 13 14]
    print(arr1 - 10)  # 矩阵减10  [-9 -8 -7 -6]
    print(arr1 * 2)  # 矩阵乘2  [ 2  4  6  8]
    print(arr1 * 2)  # 矩阵乘2  [ 2  4  6  8]

    print(arr1 + arr2)  # 矩阵相加   维度大小相同的数组 相加   [ 7  9 11 13]
    print(arr1 - arr2)  # 矩阵相减  维度大小相同的数组 相减    [-5 -5 -5 -5]
    print(arr2 - arr1)  # 矩阵相减  维度大小相同的数组 相减    [5 5 5 5]
    print(arr1 * arr2)  # 矩阵相乘  维度大小相同的数组 相乘  [ 6 14 24 30]


# 2. 初始化特殊数组：zeros、ones
def demo_zeros_ones():
    print("\n===============demo_zeros_ones=================")
    arr0_1d = np.zeros(2, )
    arr0 = np.zeros(2, dtype=int)
    arr1 = np.zeros((2, 3), dtype=int)
    arr2 = np.ones((2, 3), dtype=int)
    print(f"np.zeros全零一维数组：{arr0_1d} {arr0}\n")
    print("np.ones全零2维(2行3列)数组：\n", arr1)
    print("np.ones全一2维(2行3列)数组：\n", arr2)


# 3. 生成序列：arange、linspace
def demo_sequence():
    print("\n===============demo_sequence=================")
    print(np.arange(6))
    arr1 = np.arange(0, 10, 2) # 线形的 固定步长为2 长度自动计算
    arr2 = np.linspace(0, 10, 5) # 线性的 固定长度 步长自适应
    print("np.arange等差序列：", arr1)       ## [0 2 4 6 8]
    print("np.linspace等距5个值：", arr2)    # [0. 2.5 5. 7.5 10.]


# 4. 数组变形与转置：reshape、T
def demo_reshape_transpose():
    print("\n==============demo_reshape_transpose==================")
    arr = np.arange(6).reshape(2, 3)
    print("reshape重塑形状(2行3列)：\n", arr)
    print("arr.T转置：\n", arr.T)


"""
1. **冒号 `:` 是切片内部的分隔符（同一个维度里）：`start:end:step`**
2. **逗号 `,` 是【不同维度之间】的分隔符**
"""
# 5. 数组切片取值
def demo_slice():
    print("\n===============demo_slice=================")
    arr = np.arange(9).reshape(3, 3)
    print("原始数组：\n", arr)
    print("取第0行所有列：", arr[0, :])

    # 行：[:2] → start=0, end=2, step=1  行下标 0,1
    # 列：0::2 → start=0, end=省略（到末尾）, step=2  列下标 0,2
    print("取前两行前两列：\n", arr[:2, 0::1])
    # 行：[:2] → start=0, end=2, step=1  行下标 0,1
    # 列：:2 → start=0, end=2, step=1  列下标 0,1
    print("取前两行前两列：\n", arr[:2, :2])


# 6. 类型转换 astype
def demo_dtype():
    print("\n===============demo_dtype=================")
    arr = np.array([1.1, 2.2, 3.3])
    arr_int = arr.astype(np.int32)
    print("原浮点数组：", arr)
    print("转为int32整数：", arr_int)


# 7. 聚合统计：sum mean max min
def demo_agg():
    print("\n===============demo_agg=================")
    arr = np.array([[1, 2], [3, 4]])
    print("数组求和sum：", arr.sum())
    print("求平均值mean：", arr.mean())
    print("最大值max：", arr.max())
    print("最小值min：", arr.min())


# 8. 矩阵点乘 dot
def demo_dot():
    print("\n==============demo_dot==================")
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    res = np.dot(a, b)
    print("矩阵点乘np.dot结果：\n", res)


# 9. 数组拼接 concatenate
def demo_concat():
    print("\n===============demo_concat=================")
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6]])
    res = np.concatenate([a, b], axis=0)
    print("竖直拼接axis=0：\n", res)


# 10. 随机数组 rand
def demo_random():
    print("\n===============demo_random=================")
    arr = np.random.rand(2, 2)
    print("0~1随机数组np.random.rand：\n", arr)


if __name__ == "__main__":
    demo_array_create_1d()
    demo_array_create_2d()
    demo_array_calc()
    demo_zeros_ones()
    demo_sequence()
    demo_reshape_transpose()
    demo_slice()
    demo_dtype()
    demo_agg()
    demo_dot()
    demo_concat()
    demo_random()
