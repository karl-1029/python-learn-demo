"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：

1．添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
    1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
    1.2 检查学生姓名是否已存在，如果学生不存在，再添加（存在则，不添加）
    1.3 验证成绩范围（0-100分）
    1.4 创建学生对象并添加到系统

2．修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
    2.1 输入要修改的学生姓名
    2.2 根据姓名查找该学生，显示该生当前成绩信息
    2.3 输入新的语文、数学、英语成绩
    2.4 更新学生成绩数据

3．删除学生成绩：根据输入的学生姓名，删除对应的学生成绩

4．查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
    4.1 输出格式为："姓名: 张三 | 语文: 85 | 数学: 90 | 英语: 88 | 总分: 263"

5．展示全部学生成绩：展示出系统中所有学生的成绩
"""


class Student:
    """
    学生类
    """

    def __init__(self, name, chinese, math, english):
        """
        初始化方法
        :param name: 姓名
        :param chinese: 语文成绩
        :param math: 数学成绩
        :param english: 英语成绩
        """
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
        self.total = chinese + math + english

    def __str__(self):
        """
        对象转字符串
        :return: 字符串
        """
        return f"姓名: {self.name} | 语文: {self.chinese} | 数学: {self.math} | 英语: {self.english} | 总分: {self.total_socre()}"

    def total_socre(self):
        """
        计算总分
        :return: 总分
        """
        return self.chinese + self.math + self.english

    def update_score(self, chinese=None, math=None, english=None):
        """
        更新成绩
        :param chinese: 语文成绩
        :param math: 数学成绩
        :param english: 英语成绩
        :return:
        """
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

        self.total = chinese + math + english



stu = Student("张三", 85, 90, 88)
print(stu)
stu.update_score(chinese=99)
print(stu)
