"""
函数参数传递
    位置参数
    关键参数

默认值参数

"""


def creat_student(name, age, sex, city):
    return {"name": name, "age": age, "sex": sex, "city": city}


print("位置参数 : ", creat_student("karl", 18, "male", "上海"))

# 位置参数没有顺序  优点：代码可读性高
print("关键字参数 : ", creat_student(name="tom", age=28, sex="male", city="上海"))
print("关键字参数 : ", creat_student(age=28, sex="male", city="上海", name="tom"))

# 位置参数+关键字参数 混合使用 位置参数 要在前面 关键字参数 要在后面
print("位置参数+关键字参数 : ", creat_student("tom", 28, sex="male", city="上海"))



print("=================================")
# 定义函数 形参带默认值
def creat_student(name, age, sex="male", city="上海"):
    return {"name": name, "age": age, "sex": sex, "city": city}
print(creat_student("karl", 18))
print(creat_student("karl", 18, "female"))
print(creat_student("karl", 18, "female", "北京"))

