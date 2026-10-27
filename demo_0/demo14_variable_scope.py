"""
变量作用域
    global 关键字
    1. global  告诉解释器，这个变量是全局变量

"""

num = 0
num_1 = 0

# 帮我生成测试作用域的代码
def demo_scope():
    num =10
    global num_1
    num_1 = 20
    print(f"in method scope num : {num} num_1num_1 : {num_1}")

demo_scope()
print(f"in global scope num : {num} num_1num_1 : {num_1}")


debug_model =  False

def enable_debug_model():
    global debug_model
    debug_model = True

def disable_debug_model():
    global debug_model
    debug_model = False

print(f"debug_model: {debug_model}")
enable_debug_model()
print(f"debug_model: {debug_model}")
disable_debug_model()
print(f"debug_model: {debug_model}")
