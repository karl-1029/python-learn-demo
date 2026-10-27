"""
测试导入模块

    定义包
        __init__.py 作用定义包的模块
"""

# import util.my_var
#
# print(util.my_var.NAME)




# from util.my_var import NAME, PI
# print(NAME)
# print(PI)




# from util import my_var
# from util import my_fun
#
# print(my_var.PI)
# print(my_var.NAME)
# print("=======测试导包=======")
# my_fun.log_print1()
# my_fun.log_print2()
# my_fun.log_print3()
# my_fun.log_print4()


from util import *

print(my_var.PI)
print(my_var.NAME)
print("=======测试导包=======")
my_fun.log_print1()
my_fun.log_print2()
my_fun.log_print3()
my_fun.log_print4()

