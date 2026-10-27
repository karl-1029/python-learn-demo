# __all__ 表示import * 代表的内容

"""
python里面的内置变量
__all__
    用来指定 from 模块 import  时允许导入的名称：
__name__
    表示模块名。直接运行这个文件时，值是 "__main__"；被其他文件导入时，值是模块名，例如 "__demo_1_myfun__"。
    常用于判断代码是否由当前文件直接运行：
"""

__all__ = ["PI","log_print1","log_print4"]

PI = 3.1415925
NAME = "karl"


def log_print1():
    print("- " * 30)


def log_print2():
    print("=" * 30)


def log_print3():
    print("+ " * 30)


def log_print4():
    print("* " * 30)

"""
__name__  是默认内置变量
    直接运行模块时，__name__ == "__main__"
    被导入后运行时模块，__name__ == 模块名也就是文件名 "demo_1_main"
"""

if __name__ == "__main__":
    print("this is __name__==__main__ call")
    log_print1()


