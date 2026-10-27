num = 0
while num < 10:
    print(f"num is {num} less than 10")
    num += 1
else:
    print(f"循环结束: num is {num} not less than 10")

while num < 20:
    print(f"num is {num} less than 20")
    num += 1

# 1-100 偶数求和
count = 0
start_num = 1
while start_num <= 100:
    if start_num % 2 == 0:
        count += start_num
    start_num += 1
print(f"1-100 偶数求和为: {count}")

msg = "hello-python"
for item in msg:
    print(f"当前字符是: {item}")
else:
    print("循环结束")

# print(*,end="") 默认换行\n
print("===================")
print("hello-world", end=" ")
print("hello-python")

print(list(range(10)))
print(list(range(1, 10)))
print(list(range(1, 10)))
print(list(range(1, 11)))
print(list(range(1, 11, 2)))
"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 3, 5, 7, 9]
"""

for index in range(10):
    print(f"当前索引是: {index}")

kuan_du = 7
chang_du = 3
for i in range(chang_du):
    for j in range(kuan_du):
        print("*", end=" ")
    print()

print("==============")
for index in range(10):
    if index == 3:
        print("当前索引是3,跳过本次循环 不往下走了 结束当前循环 执行下次循环")
        continue

    if index == 7:
        print("当前索引是7,跳出循环 结束整个循环")
        break

    print(f"当前索引是: {index}")
