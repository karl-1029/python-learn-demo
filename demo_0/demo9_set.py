"""
根据提供的班级学生的选课情况，完成如下需求：
1. 找出同时选修了法语和艺术的学生
2. 找出同时选修了所有四门课程的学生
3. 找出选修了足球，但是没有选修篮球的学生
4. 统计每一个学生选修的课程数量
"""

# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1. 找出同时选修了法语和艺术学生的名单
result = french_set.intersection(art_set)
print(type(result), result)
result_intersection = french_set & art_set
print(result_intersection)

# 2. 找出同时选修了所有四门课程的学生
# 交集
result = football_set.intersection(basketball_set, french_set, art_set)
result_intersection = football_set & basketball_set & french_set & art_set
print(type(result), result)
print(result_intersection)

# 3. 找出选修了足球，但是没有选修篮球的学生
# 差集
result = football_set.difference(basketball_set)
result_difference = football_set - basketball_set
print(result)
print(result_difference)


# 4. 统计每一个学生选修的课程数量
# 并集
all_students_distinct = football_set.union(basketball_set).union(french_set).union(art_set)
print(all_students_distinct)
all_students_distinct = football_set | basketball_set | french_set | art_set
print(all_students_distinct)

all_students_list = [*football_set, *basketball_set, *french_set, *art_set]
print(all_students_list)
for item in all_students_distinct:
    print(f"姓名：{item}，一共选修了{all_students_list.count(item)}门课程")
