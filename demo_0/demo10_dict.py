"""
字典
    3.7 以后有序
    key不可以重新
    key必须是不可变
"""
# 定义字典
def_dict = {}
def_dict_empty = dict()
print(type(def_dict))
print(def_dict)
print(type(def_dict_empty))
print(def_dict_empty)


print("=========字典crud==========")

# dict_demo = {"name": "karl", "age": 18, "sex": "male",10:20,[]:"list_value"}   TypeError: unhashable type: 'list'
dict_demo = {"张三": 10, "李四": 20, "王五": 30, "赵四": 40, "王六": 50}
print(dict_demo)

# 访问
print(dict_demo["张三"])
print(dict_demo.get("张三"))

# 添加
dict_demo["karl"] = 100
print(dict_demo)

# 修改value
dict_demo["张三"] = 99
print(dict_demo)

# 删除
dict_demo.pop("张三")
print(dict_demo)
del dict_demo["karl"]
print(dict_demo)


print("=========字典crud==========")
def_dict = {"name": "karl", "age": 18, "sex": "male"}
print(def_dict.keys())
print(def_dict.values())
print(def_dict.items())
