# set     集合


"""
无序 不可重复 可修改
"""
set_demo_0 = set()
set_demo_1 = {1, 2, 3, 5, 10, "500", 1, 5, 400}
print(type(set_demo_1))
print(set_demo_1)  # <class 'dict'>  字典类型

set_demo_2 = {9, 2, 3, 5, 2, 10, 0, 4}
print(f"类型:{type(set_demo_2)}  数据:{set_demo_2}")

print("==========集合方法==========")
set_demo = {100,200,300,400,500,600,700,800,900,1000}
print(f"init data:{set_demo}")
set_demo.add(10)
print(f"after add:{set_demo}")

# 删除指定元素
set_demo.remove(100)
print(f"删除指定元素:{set_demo}")

# 随机删除任意一个元素
del_element = set_demo.pop()
print(f"随机删除一个元素:{set_demo}  被随机删除的:{del_element}")

# # 删除所有元素
set_demo.clear()
print(f"清空所有元素后:{set_demo}")


print("==========集合运算==========")
s1 = {"A", "B", "C", "D", "E", "F"}
s2 = { "D", "E", "F","H", "I", "J"}
# 求并集
print("=========求并集")
s_result = s1.union(s2)
print(s_result) #{'F', 'I', 'C', 'J', 'B', 'E', 'A', 'H', 'D'}
print(s1 | s2)

# 求交集
print("=========求交集")
s_result = s1.intersection(s2)
print(s_result)

# 求差集
print("=========求差集")
s_result_1 = s1.difference(s2)
s_result_2 = s2.difference(s1)
print(s_result_1)
print(s_result_2)