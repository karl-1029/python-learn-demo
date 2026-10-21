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
def demo_array_create():
    print("\n======== 分隔线，区分不同demo输出")
    lst = [1, 2, 3, 4]
    arr = np.array(lst)
    print("np.array创建数组：", arr)
    print("数组类型：", type(arr))
    print("数组维度：", arr.ndim)
    print("数组形状：", arr.shape)

# 2. 初始化特殊数组：zeros、ones
def demo_zeros_ones():
    print("\n======== 分隔线，区分不同demo输出")
    arr0 = np.zeros((2, 3))
    arr1 = np.ones((2, 3))
    print("np.zeros全零数组：\n", arr0)
    print("np.ones全一数组：\n", arr1)

# 3. 生成序列：arange、linspace
def demo_sequence():
    print("\n======== 分隔线，区分不同demo输出")
    arr1 = np.arange(0, 10, 2)
    arr2 = np.linspace(0, 10, 5)
    print("np.arange等差序列：", arr1)
    print("np.linspace等距5个值：", arr2)

# 4. 数组变形与转置：reshape、T
def demo_reshape_transpose():
    print("\n======== 分隔线，区分不同demo输出")
    arr = np.arange(6).reshape(2, 3)
    print("reshape重塑形状(2行3列)：\n", arr)
    print("arr.T转置：\n", arr.T)

# 5. 数组切片取值
def demo_slice():
    print("\n======== 分隔线，区分不同demo输出")
    arr = np.arange(9).reshape(3, 3)
    print("原始数组：\n", arr)
    print("取第0行所有列：", arr[0, :])
    print("取前两行前两列：\n", arr[:2, :2])

# 6. 类型转换 astype
def demo_dtype():
    print("\n======== 分隔线，区分不同demo输出")
    arr = np.array([1.1, 2.2, 3.3])
    arr_int = arr.astype(np.int32)
    print("原浮点数组：", arr)
    print("转为int32整数：", arr_int)

# 7. 聚合统计：sum mean max min
def demo_agg():
    print("\n======== 分隔线，区分不同demo输出")
    arr = np.array([[1, 2], [3, 4]])
    print("数组求和sum：", arr.sum())
    print("求平均值mean：", arr.mean())
    print("最大值max：", arr.max())
    print("最小值min：", arr.min())

# 8. 矩阵点乘 dot
def demo_dot():
    print("\n======== 分隔线，区分不同demo输出")
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    res = np.dot(a, b)
    print("矩阵点乘np.dot结果：\n", res)

# 9. 数组拼接 concatenate
def demo_concat():
    print("\n======== 分隔线，区分不同demo输出")
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6]])
    res = np.concatenate([a, b], axis=0)
    print("竖直拼接axis=0：\n", res)

# 10. 随机数组 rand
def demo_random():
    print("\n======== 分隔线，区分不同demo输出")
    arr = np.random.rand(2, 2)
    print("0~1随机数组np.random.rand：\n", arr)


if __name__ == "__main__":
    demo_array_create()
    demo_zeros_ones()
    demo_sequence()
    demo_reshape_transpose()
    demo_slice()
    demo_dtype()
    demo_agg()
    demo_dot()
    demo_concat()
    demo_random()
