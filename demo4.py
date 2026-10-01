"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!数据容器!!!!!!!!!!!!!!!!!!!!!!!!!
str     字符串
list    列表
tuple   元组
dict    字典
set     集合
"""

# 列表！！！！！！！！！！！！！！！！！！！！！

list_demo1 = [40, 89, 88, "dadf", True, False, 3.14]
print(type(list_demo1))
print(list_demo1)  # [40, 89, 88, 'dadf', True, False, 3.14]
print(list_demo1[0])  # 访问列表第一个元素   40
print(list_demo1[-1])  # 访问列表最后一个元素 3.14
print(list_demo1[2:5])  # 访问列表第3到第5个元素  [88, 'dadf', True]

print("===============")
# 修改
print(list_demo1)
list_demo1[3] = "hello"  # 修改列表第4个元素
print(list_demo1)

# 删除
print("长度: ", len(list_demo1), ", 内容: ", list_demo1, )
del list_demo1[0]
print("删除第一个元素后: ", len(list_demo1), ", 内容: ", list_demo1, )

# 遍历list
for item in list_demo1:
    print(item)

#  list[start_index:end_index:step]
print("========列表切片(截取)=======")
list_demo2 = ["A", "B", "C", "D", "E", "F"]
print(list_demo2)
print(list_demo2[0:2])  # ['A', 'B', 'C']
print(list_demo2[:3])  # ['A', 'B', 'C']
print(list_demo2[::2])  # ['A', 'C', 'E']
print(list_demo2)  # ['A', 'B', 'C']

print("========列表基础方法CRUD=======")

# 添加元素
list_num = [10, 11, 12, 13, 14, 15]
print(list_num)

list_num.append(16)
print(list_num)

list_num.insert(0, 9)
print(list_num)
list_num.insert(2, 10.5)
print(list_num)

print("===========================")

# 删除元素
list_num = [10, 11, 12, 12.5, 13, 14, 15]
print(list_num)
list_num.remove(12.5)
print(list_num)  # [10, 11, 12, 13, 14, 15]
list_num.pop()
print(list_num)  # [10, 11, 12, 13, 14]
list_num.pop(2)
print(list_num)  # [10, 11, 13, 14]

print("=============排序==============")
list_num = [10, 11, 12, 13, 14, 15]
print(list_num)
list_num.reverse()
print(list_num)
print("=============排序1==============")
list_sort = [15, 50, 14, 1, 174, 85]
print(list_sort)
list_sort.sort()  # 默认升序
print(list_sort)
print("=============排序2==============")
list_sort = [15, 50, 14, 1, 174, 85]
print(list_sort)
list_sort.sort(reverse=False)  # 升序
print(list_sort)
list_sort.sort(reverse=True)  # 降序
print(list_sort)

print("=========最大/小值 求和 对一个list 数值==================")
list_count = [110, 11, 120, 13, 14, 15, -1]
print(max(list_count))
print(min(list_count))
print(sum(list_count))

print("===========================")
# 合并列表
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6, 7]

merge_list1 = []
for item in list1:
    merge_list1.append(item)
for item in list2:
    merge_list1.append(item)
print(merge_list1)

merge_list2 = list1 + list2
print(merge_list2)

# *list 表示拆包
merge_list3 = [*list1, *list2]
print(merge_list3)

# 列表求交集（重复元素）
union_list1 = []
for item in list1:
    if item in list2:
        union_list1.append(item)
print(union_list1)

# 列表去重
unique_list1 = []
for item in list1:
    if item not in list2:
        unique_list1.append(item)
print(unique_list1)

# 求平方 （列表推导式）
source_num = [1, 2, 3, 4, 5]
# 传统思维
squares1 = []
squares2 = []
for item in source_num:
    squares1.append(item * item)
    squares2.append(item ** 2)
print(squares1)
print(squares2)

# ****列表推导 语法格式 **** [表达式 for 元素 in 列表]
squares3 = [item ** 2 for item in source_num]
print(squares3)
# ****列表推导 语法格式 **** [表达式 for 元素 in 列表 if 条件]  求偶数平方根
squares4 = [item ** 2 for item in source_num if item % 2 == 0]
print(squares4)
