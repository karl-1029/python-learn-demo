print("hello world")
print('hello world')
print('hello "ddd" world')
print('hello "ddd" world')
print("hello world" " 2 hello world")
print("hello world" +" 2 hello world")
print("this is line 1 \nthis is line 2")


description = "this is str"
print(type(description))
description=123
print(type(description))
description=123.66
print(type(description))
description=True
print(type(description))
print("====================")

full_name = input("please input your full name: ")
full_age = input("please input your full age: ")
print("full_name:" + full_name + ", full_age:" + full_age)


print("====================")

name="karl"
age=12
print("name is %s and age is %s" % (name, age))
print("name is %s and age is %d" % (name, age+50))
print("name is {name} and age is {age+100}")
# format placeholder
print(f"name is {name} and age is {age}")

print("====================")

score = 90
if score>90:
    print("score is great")
else:
    print("score is good")
