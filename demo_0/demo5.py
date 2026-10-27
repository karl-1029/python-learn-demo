"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!数据容器!!!!!!!!!!!!!!!!!!!!!!!!!
str     字符串
list    列表
tuple   元组
dict    字典
set     集合
"""

# 字符串！！！！！！！！！！！！！！！！！！！！！
demo_str = "hello-python"
# TypeError: 'str' object does not support item assignment   字符串不可变
# demo_str[0] = "can change?"

print(demo_str[0])
print(demo_str[1])
for item in demo_str:
    print(item)

print("===========")
# 切片
print(demo_str[0:5])
print(demo_str[0:5:2])

print("============================================")
str_test = "hello-world-hello-python"

s_find = str_test.find("hello")
print(type(s_find),s_find)

s_count = str_test.count("hello")
print(type(s_count),s_count)

s_format = "hello {} {}".format("karl", "python")
print(type(s_format),s_format)

s_upper = str_test.upper()
s_lower = str_test.lower()
print(type(s_upper),s_upper)
print(type(s_lower),s_lower)

s_replace = str_test.replace("hello","cao")
print(type(s_replace),s_replace)

s_split = str_test.split("-")
print(type(s_split),s_split)

s_start_with = str_test.startswith("cao")
print(type(s_start_with),s_start_with)
