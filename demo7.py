# 元组 demo


"""
## 💡解答
根据如下提供的学生成绩单，完成如下需求：
1. 计算每个学生的总分、各科平均分，然后一并输出出来。
2. 统计各科成绩的最低分、最高分、平均分，并输出。
3. 查找成绩优秀（平均分大于90）的学生，并输出。

姓名 学号 语文 数学 英语 所在地
"""

students = (
    ("karl", "id_001", 96, 98, 80, "湖北"),
    ("tom", "id_002", 90, 80, 92, "北京"),
    ("lucy", "id_003", 95, 90, 100, "上海"),
    ("lily", "id_004", 90, 100, 90, "广州"),
    ("lucy", "id_005", 80, 90, 100, "深圳"),
    ("lily", "id_006", 90, 78, 90, "杭州"),
    ("lucy", "id_007", 80, 70, 100, "西安"),
    ("lily", "id_008", 90, 67, 90, "南京")
)

# 统计每个学生总分/平均分
print("姓名\t\t学号\t\t总分\t\t平均分\t\t所在地")
for item in students:
    total_score = item[2] + item[3] + item[4]
    avg_score = total_score / 3
    print(f"{item[0]} {item[1]}  {total_score}  {avg_score:.2f}  {item[5]}")


print("===========================")

# print("各科成绩最低分、最高分、平均分")  {avg:.2f} 表示小数去2个小数
chinese_score = [item[2] for item in students]
math_score = [item[3] for item in students]
english_score = [item[4] for item in students]
print(f"语文 最低分:{min(chinese_score)} 最高分:{max(chinese_score)} 平均分:{sum(chinese_score)/len(chinese_score):.2f}")
print(f"数学 最低分:{min(math_score)} 最高分:{max(math_score)} 平均分:{sum(math_score)/len(math_score):.2f}")
print(f"英语 最低分:{min(english_score)} 最高分:{max(english_score)} 平均分:{sum(english_score)/len(english_score):.2f}")


print("===========================")

print("计算成绩优秀（平均分大于90）的学生")
for item in students:
    avg = (item[2] + item[3] + item[4]) / 3
    if avg > 90:
        print(f"{item[0]} {item[1]} {avg:.2f}")