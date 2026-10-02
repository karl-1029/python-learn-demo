"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!数据容器!!!!!!!!!!!!!!!!!!!!!!!!!
str     字符串
list    列表
tuple   元组
dict    字典
set     集合
"""

# 元组！！！！！！！！！！！！！！！！！！！！！

"""
元组的特性 
有序、允许重复、不可变(不支持动态crud)、
支持索引切片和混合类型，并补充单元素元组逗号写法及浅不可变注意点。

和列表的区别: 元组不可变，列表可变


组包是把多个值合成一个元组，例如 point = 3, 5（等价于 (3, 5)）；解包是把可迭代对象中的值依次赋给变量，例如 x, y = point。
变量数通常要与元素数一致，也可以用  接收剩余值：first, rest = (1, 2, 3)，结果是 first == 1、rest == [2, 3]。
*通常表示接收剩余的值的语法是 *name，例如 *args = (1, 2, 3)，结果是 args == [1, 2, 3]。

"""

# 定义元组
demo_tuple_1 = ("hello", "python")
demo_tuple_2 = ("hello", "hello", 22, True)
demo_tuple_3 = tuple()
demo_tuple_4 = (100,)
print(type(demo_tuple_1), demo_tuple_1)
print(type(demo_tuple_2), demo_tuple_2)
print(type(demo_tuple_3), demo_tuple_3)
print(type(demo_tuple_4), demo_tuple_4)

# 访问元组元素
print(demo_tuple_1[0])
print(demo_tuple_1[-1])

print("==========================")

# 基本方法 切片 索引访问 迭代
demo_tuple_1 = ("hello", "python", "cao", "java", "c++", "python")
print("长度 ", len(demo_tuple_1))
print("数量 ", demo_tuple_1.count("python"))
print("切片截取: %s  %s" % (type(demo_tuple_1[0:2]), demo_tuple_1[0:2]))
print("获取index:  %s  %s" % (type(demo_tuple_1.index("python")), demo_tuple_1.index("python")))

# TypeError: 'tuple' object does not support item assignment 元组不能修改
# demo_tuple_1[0] = 500

for item in demo_tuple_1:
    print(item)

print("=========组包解包===========")

tuple_demo_1 = (1, 2, 3, 4, 5)
tuple_demo_2 = 1, 2, 3, 4, 5
print(type(tuple_demo_1), tuple_demo_1)
print(type(tuple_demo_2), tuple_demo_2)

a,b,c,d,e = tuple_demo_1
print(a,b,c,d,e)
first,*others,last = tuple_demo_1
print(first,others,last)
*a,b,c = tuple_demo_1
print(a,b,c)


print("=========组包解包  交换变量===========")
a=10
b=20
temp= (b,a)
temp_1= b,a
a,b = temp_1
print(a,b)

# 简洁写法
a=10
b=20
a,b = b,a
print(a,b)

