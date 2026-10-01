# score = input("please input your score: ")
from re import match

score = 30
source_int = int(score)
if source_int > 90:
    print("score is great")
else:
    print("score is good")

if source_int > 90:
    print("score is great")
elif source_int > 80:
    print("score is good")
else:
    print("score is bad")

print("=====================")

flag = True
if flag:
    print("flag is true")

name1 = "karl"
if name1:
    print(f"name1 is not empty: {name1}")

name2 = ""
if name2:
    print(f"name2 is not empty: {name2}")

name3 = None
if name3:
    print(f"name3 is not empty: {name3}")

age1 = 20
if age1:
    print(f"age1 is not empty {age1}")

age2 = 0
if age2:
    print(f"age2 is not empty {age2}")

age3 = -2
if age3:
    print(f"age3 is not empty {age3}")


# 单行注释


"""
if 变量名:
    print("条件成立")

原理：Python会把变量自动转为 ** 布尔值（bool） ** ，这个叫 ** 隐式布尔判断 **

## ✅ 哪些值会被当成 True（真值）
- 非0
数字：`1`、`99`、`-5`、`3.14`
- 非空字符串：`"abc"`、`"0"`
- 非空容器：`[1, 2]`、`{"name": "a"}`、`(1,)`

## ❌ 哪些值会被当成 False（假值，if 不执行）
- `0`、`0.0`
- `None`
- 空字符串
`""`
- 空列表
`[]`、空字典
`{}`、空元组
`()`

"""

day=input("今天是星期几(1-7):")
match day:
    case "1":
        print("今天是星期一")
    case "2":
        print("今天是星期二")
    case "3":
        print("今天是星期三")
    case "4":
        print("今天是星期四")
    case "5":
        print("今天是星期五")
    case "6":
        print("今天是星期六")
    case "7":
        print("今天是星期日")
    case _:
        print("输入有误")