"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：

添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
1.2 检查学生姓名是否已存在，如果学生不存在，再添加（存在则，不添加）
1.3 验证成绩范围（0-100分）
1.4 创建学生对象并添加到系统
修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
2.1 输入要修改的学生姓名
2.2 根据姓名查找该学生，显示该生当前成绩信息
2.3 输入新的语文、数学、英语成绩
2.4 更新学生成绩数据
删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
4.1 输出格式为：“姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263”
展示全部学生成绩：展示出系统中所有学生的成绩
"""
from student import Student


class EduMangment:
    system_version = "1.0.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("请输入学生姓名：")

        for item in self.students:
            if item.name == name:
                print("学生已存在")
                return

        chinese = int(input("请输入学生语文成绩："))
        math = int(input("请输入学生数学成绩："))
        english = int(input("请输入学生英语成绩："))

        if 0 < chinese <= 100 and 0 < math <= 100 and 0 < english <= 100:
            student = Student(name, chinese, math, english)
            self.students.append(student)
            print("添加学生成功")
        else:
            print("成绩范围错误!0-100之间")
            return

    def update_student(self):
        name = input("请输入学生姓名：")
        for item in self.students:
            if item.name == name:
                chinese = int(input("请输入学生语文成绩："))
                math = int(input("请输入学生数学成绩："))
                english = int(input("请输入学生英语成绩："))
                if 0 < chinese <= 100 and 0 < math <= 100 and 0 < english <= 100:
                    item.update_score(chinese, math, english)
                    print("修改学生成功")
                else:
                    print("成绩范围错误!0-100之间")
                return

        print("学生不存在")

    def delete_student(self):
        name = input("请输入学生姓名：")
        for item in self.students:
            if item.name == name:
                self.students.remove(item)
                print("删除成功")
                return

        print("学生不存在")

    def query_student(self):
        name = input("请输入学生姓名：")
        for item in self.students:
            if item.name == name:
                print(item)
                return
        print("学生不存在")

    def list_student(self):
        for item in self.students:
            print(item)

    def run(self):
        mean = """
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
*       1:添加学生  2:修改学生  3:删除学生  4:查询指定学生  5:展示全部学生 * 6:退出系统          * * 
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
        """

        print(f"欢迎来到{self.system_name} version:{self.system_version}")

        while True:
            print(mean)
            choice = input("请输入功能编号：")
            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.delete_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.list_student()
                    case "6":
                        print("退出系统")
                        break
                    case _:
                        print("输入错误,请重新输入1-6之间")
            except Exception as e:
                print("run 方法异常",e)


if __name__ == "__main__":
    edu = EduMangment()
    edu.run()
