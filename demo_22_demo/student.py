"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：

添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
展示全部学生成绩：展示出系统中所有学生的成绩
"""


class Student:

    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
        self.total_score = chinese + math + english

    def update_score(self, chinese, math, english):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

        self.total_score = chinese + math + english


    def __str__(self) -> str:
        return f"姓名：{self.name}，语文：{self.chinese}，数学：{self.math}，英语：{self.english}，总分：{self.total_score}"


if __name__ == "__main__":
    stu = Student("tom", 90, 80, 70)
    print(stu)